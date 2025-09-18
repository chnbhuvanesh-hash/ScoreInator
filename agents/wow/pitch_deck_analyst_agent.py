class PitchDeckAnalystAgent:
    def __init__(self, name="Pitch Deck Analyst"):
        self.name = name
    
    def run(self, context):
        """
        Runs the pitch deck analysis.
        Expects `context` to contain 'presentation_url'.
        """
        presentation_url = context.get("presentation_url")

        # For the hackathon, this is still a mock analysis.
        # Real-world: use python-pptx, PDF parser, or CV model depending on input type.
        
        analysis_score = 75
        feedback = (
            "The pitch deck seems to be well-structured. "
            "It clearly defines the problem and solution. "
            "Consider adding a slide on your project's technical architecture."
        )
        
        result = {
            "analysis_score": analysis_score,
            "feedback": feedback,
            "score": analysis_score
        }

        # Save result back into context (so later agents can use it)
        context["pitchdeck_report"] = result
        return result
