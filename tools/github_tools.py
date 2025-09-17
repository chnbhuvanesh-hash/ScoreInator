# score-inator/tools/github_tools.py
"""
Github helpers: validate URLs and fetch README and repo metadata.

Notes:
- If GITHUB_TOKEN is provided (or token argument), will use it to increase rate limits.
- Uses the GitHub REST API for repo metadata and raw.githubusercontent.com for raw README fallback.
"""

import re
from typing import Tuple, Optional, Dict, Any
import requests

GITHUB_API = "https://api.github.com"

def validate_github_url(url: str) -> Tuple[bool, Optional[Dict[str,str]]]:
    """
    Very simple regex-based validation. Returns (True, {"owner":.., "repo":..}) when valid.
    Accepts URLs like:
      - https://github.com/owner/repo
      - https://github.com/owner/repo/
      - https://github.com/owner/repo.git
    """
    if not url:
        return False, None
    url = url.strip()
    # remove trailing .git or slash
    url_nogit = re.sub(r"\.git$", "", url.rstrip("/"))
    m = re.match(r"^https?://github\.com/([^/]+)/([^/]+)$", re.sub(r"https?://", "https://", url_nogit))
    if not m:
        # try to parse more flexibly
        parts = url_nogit.split("/")
        try:
            idx = parts.index("github.com")
            owner = parts[idx+1]
            repo = parts[idx+2]
            # strip .git if any
            repo = re.sub(r"\.git$", "", repo)
            return True, {"owner": owner, "repo": repo}
        except Exception:
            return False, None
    owner, repo = m.group(1), m.group(2)
    return True, {"owner": owner, "repo": repo}

def _request_github_api(path: str, token: Optional[str] = None) -> requests.Response:
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": "score-inator/1.0"}
    if token:
        headers["Authorization"] = f"token {token}"
    url = GITHUB_API + path
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()
    return resp

def fetch_readme_and_repo_info(owner: str, repo: str, token: Optional[str] = None) -> Tuple[str, Dict[str,Any]]:
    """
    Attempts to fetch:
      - README.md text (best-effort)
      - repo metadata: description, default_branch, url, license presence, CI presence hints, tests presence hint
    Returns (readme_text or "", repo_info dict)
    """
    repo_info = {"owner": owner, "name": repo, "url": f"https://github.com/{owner}/{repo}"}
    # 1. Get repo metadata
    try:
        r = _request_github_api(f"/repos/{owner}/{repo}", token=token)
        j = r.json()
        repo_info["description"] = j.get("description")
        repo_info["default_branch"] = j.get("default_branch") or "main"
        repo_info["private"] = j.get("private", False)
        # license
        repo_info["license"] = bool(j.get("license"))
    except requests.HTTPError as e:
        raise RuntimeError(f"Repo metadata request failed: {e}")

    # 2. Attempt to fetch README via API (preferred)
    readme_text = ""
    try:
        r = _request_github_api(f"/repos/{owner}/{repo}/readme", token=token)
        # API returns base64 content usually
        j = r.json()
        content = j.get("content")
        encoding = j.get("encoding", "")
        if content and encoding == "base64":
            import base64
            readme_text = base64.b64decode(content).decode("utf-8", errors="replace")
    except requests.HTTPError:
        # fallback to raw content (raw.githubusercontent.com)
        pass

    # 3. Fallback raw README path using default branch
    if not readme_text:
        default_branch = repo_info.get("default_branch", "main")
        possible_paths = [
            f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/README.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/README.MD",
            f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/readme.md",
        ]
        for raw_url in possible_paths:
            try:
                r = requests.get(raw_url, timeout=10)
                if r.status_code == 200 and r.text.strip():
                    readme_text = r.text
                    break
            except requests.RequestException:
                continue

    # 4. Check some repository files: license file, tests folder, .github/workflows
    files = {}
    try:
        # list top-level files
        r = _request_github_api(f"/repos/{owner}/{repo}/contents", token=token)
        contents = r.json()
        names = [c.get("name", "").lower() for c in contents if isinstance(c, dict)]
        files["license"] = any(n.startswith("license") for n in names)
        files["has_tests"] = any(n in ("tests", "test") for n in names)
        files["has_ci"] = any(n == ".github" for n in names)  # coarse indicator
        # Look inside .github for workflows (if exists)
        if ".github" in names:
            try:
                r2 = _request_github_api(f"/repos/{owner}/{repo}/contents/.github/workflows", token=token)
                if r2.status_code == 200:
                    files["has_ci"] = True
            except requests.HTTPError:
                pass
    except requests.HTTPError:
        # ignore file checks if unauthenticated request blocked
        pass

    repo_info["files"] = files
    return readme_text or "", repo_info
