import random

class PitchDeckAnalystAgent:
    def __init__(self, name="Pitch Deck Analyst"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url: str):
        """
        Simulated pitch deck analysis.
        Later: Could integrate with AI to analyze actual slides or PDF.
        """

        # Sample feedback components
        feedbacks = [
            "The pitch deck is well-structured with clear problem and solution statements.",
            "Consider adding a slide on your project's technical architecture.",
            "Add visuals/charts to highlight market potential.",
            "Include a roadmap slide with milestones and timelines.",
            "Clarify target audience and user persona in a dedicated slide."
        ]

        # Randomly pick 2–3 feedback points
        selected_feedback = random.sample(feedbacks, random.randint(2, 3))

        # Assign a score between 60–90 for realistic variability
        analysis_score = random.randint(60, 90)

        return {
            "valid": True,
            "analysis_score": analysis_score,
            "feedback": " ".join(selected_feedback),
            "summary": f"Pitch deck reviewed with score {analysis_score} for {github_url}"
        }
