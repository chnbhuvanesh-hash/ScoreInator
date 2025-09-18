import random

class ArchitectAgent:
    def __init__(self, name="Architect"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url: str):
        """
        Simulate architectural assessment.
        Later we can integrate with GitHub API to fetch repo files.
        """

        # Simulated checks (randomized for demo)
        docs_present = random.choice([True, False])
        license_present = random.choice([True, False])
        project_structure = random.choice(["well_structured", "average", "poor"])

        # Score calculation
        score = 0
        if docs_present:
            score += 20
        if license_present:
            score += 15

        if project_structure == "well_structured":
            score += 25
        elif project_structure == "average":
            score += 10
        else:
            score += 0

        score = max(0, min(100, score))  # clamp 0–100

        return {
            "valid": True,
            "docs_present": docs_present,
            "license_present": license_present,
            "project_structure": project_structure,
            "score": score
        }
