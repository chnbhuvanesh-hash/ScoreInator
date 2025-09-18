import random
import requests
from tools.github_tools import GithubClient

class CodeQualityAgent:
    def __init__(self, name="Code Quality"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url: str):
        """
        Fake but more realistic static analysis simulation.
        In production: integrate with linters, SonarQube, etc.
        """
        # Simulated lint results (randomized for demo purposes)
        lint_errors = random.randint(0, 20)
        lint_warnings = random.randint(0, 15)

        # Simulated coverage percentage
        coverage_percent = random.randint(40, 95)

        # Scoring logic
        # Lower errors => higher score
        lint_score = max(0, 100 - (lint_errors * 3 + lint_warnings * 2))
        coverage_score = coverage_percent

        # Weighted average
        final_score = round((lint_score * 0.6) + (coverage_score * 0.4), 2)

        return {
            "valid": True,
            "lint_errors": lint_errors,
            "lint_warnings": lint_warnings,
            "coverage": f"{coverage_percent}%",
            "score": final_score
        }
