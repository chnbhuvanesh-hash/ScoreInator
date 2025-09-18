import requests
from tools.github_tools import GithubClient

class CodeScoutAgent:
    def __init__(self, name="Code Scout"):
        self.name = name
        self.github_client = GithubClient()

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url):
        try:
            if not github_url.startswith("https://github.com/"):
                return {"valid": False, "reason": "Invalid GitHub URL format.", "score": 0}
            
            repo_path = "/".join(github_url.split('/')[-2:])
            repo_data = self.github_client.get_repo_info(repo_path)
            
            if "message" in repo_data and repo_data["message"] == "Not Found":
                return {"valid": False, "reason": "Repository not found.", "score": 0}

            return {
                "valid": True,
                "stars": repo_data.get("stargazers_count", 0),
                "forks": repo_data.get("forks_count", 0),
                "last_commit_date": repo_data.get("pushed_at", "N/A"),
                "score": 100  # Placeholder score
            }
        except Exception as e:
            return {"valid": False, "reason": f"An error occurred: {str(e)}", "score": 0}
