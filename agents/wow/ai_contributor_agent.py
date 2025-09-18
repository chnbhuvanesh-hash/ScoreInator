import random

class AIContributorAgent:
    def __init__(self, name="AI Contributor"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_contribution(github_url)

    def run_contribution(self, github_url: str):
        """
        Simulated AI contribution agent.
        Later: Replace with OpenAI API or LLM-based code review.
        """

        # Sample suggestions
        suggestions = [
            {
                "area": "Code Quality",
                "issue": "Some functions exceed 50 lines, reducing readability.",
                "recommendation": "Refactor long functions into smaller modular helpers.",
                "difficulty": "Medium"
            },
            {
                "area": "Documentation",
                "issue": "README lacks setup instructions for local development.",
                "recommendation": "Add installation and setup guide to README.md.",
                "difficulty": "Easy"
            },
            {
                "area": "Testing",
                "issue": "Low unit test coverage detected in core modules.",
                "recommendation": "Add unit tests for data validation and error handling logic.",
                "difficulty": "Hard"
            },
            {
                "area": "Best Practices",
                "issue": "Variable naming inconsistency (snake_case vs camelCase).",
                "recommendation": "Enforce naming conventions via a linter (e.g., flake8 or pylint).",
                "difficulty": "Easy"
            }
        ]

        # Randomly pick 2–3 suggestions each run
        selected = random.sample(suggestions, random.randint(2, 3))

        return {
            "valid": True,
            "contributions": selected,
            "summary": f"{len(selected)} actionable suggestions for {github_url}"
        }
