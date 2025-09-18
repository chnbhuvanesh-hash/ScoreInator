import random

class CommunityManagerAgent:
    def __init__(self, name="Community Manager"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url: str):
        """
        Fake but realistic simulation of community health.
        In production: pull real stats from GitHub API.
        """
        # Simulated stats
        contributors = random.randint(1, 50)
        open_issues = random.randint(0, 30)
        open_prs = random.randint(0, 15)

        # Scoring logic
        score = contributors * 5 + open_prs * 3 - open_issues * 2
        score = max(0, min(100, score))  # clamp 0-100

        return {
            "valid": True,
            "contributors": contributors,
            "open_issues": open_issues,
            "open_prs": open_prs,
            "score": score
        }
