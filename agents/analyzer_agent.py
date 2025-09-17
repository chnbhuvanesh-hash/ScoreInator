import requests
from google import adk


@adk.agent()
def analyzer_agent(context: adk.Context, github_url: str) -> dict:
    """
    Analyzer & Scorer Agent.
    Fetches README.md from GitHub repo, analyzes it, and assigns a score.

    Args:
        context (adk.Context): ADK context object.
        github_url (str): GitHub repository URL.

    Returns:
        dict: { "summary": str, "score": int }
    """
    try:
        # Construct raw README URL
        parts = github_url.rstrip("/").split("/")
        if len(parts) < 5:
            return {"summary": "Invalid GitHub URL format.", "score": 0}

        owner, repo = parts[-2], parts[-1]
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md"

        response = requests.get(raw_url)
        if response.status_code != 200:
            return {"summary": "README.md not found or inaccessible.", "score": 0}

        readme_content = response.text

        # Basic heuristic scoring
        score = 5
        if "installation" in readme_content.lower():
            score += 1
        if "usage" in readme_content.lower():
            score += 1
        if "license" in readme_content.lower():
            score += 1
        if "contributing" in readme_content.lower():
            score += 1
        if "architecture" in readme_content.lower() or "design" in readme_content.lower():
            score += 1

        score = min(score, 10)

        summary = (
            f"Project `{repo}` by `{owner}`.\n\n"
            f"README.md Overview:\n\n{readme_content[:500]}...\n\n"
            f"(truncated for brevity)"
        )

        return {"summary": summary, "score": score}

    except Exception as e:
        return {"summary": f"Error analyzing repository: {str(e)}", "score": 0}
