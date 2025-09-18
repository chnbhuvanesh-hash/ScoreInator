import random
from datetime import datetime, timedelta

class CodeScoutAgent:
    def __init__(self, name="Code Scout"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url: str):
        """
        Simulated repository scout agent.
        Later: Replace with real GitHub API calls.
        """

        # Simulated values
        stars = random.randint(0, 500)
        forks = random.randint(0, 100)
        contributors = random.randint(1, 50)

        # Simulate recent commit activity
        last_commit_date = random.choice([
            (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
            "N/A"
        ])

        # Simulate project structure presence
        has_src = random.choice([True, False])
        has_tests = random.choice([True, False])
        has_docs = random.choice([True, False])

        # Scoring logic
        score = 0
        score += min(20, stars // 25)        # max 20 from stars
        score += min(10, forks // 10)        # max 10 from forks
        if last_commit_date != "N/A":
            score += 10
        if has_src:
            score += 10
        if has_tests:
            score += 10
        if has_docs:
            score += 10
        score += min(30, contributors)       # contributors boost

        score = max(0, min(100, score))

        return {
            "valid": True,
            "stars": stars,
            "forks": forks,
            "contributors": contributors,
            "last_commit_date": last_commit_date,
            "has_src": has_src,
            "has_tests": has_tests,
            "has_docs": has_docs,
            "score": score
        }
