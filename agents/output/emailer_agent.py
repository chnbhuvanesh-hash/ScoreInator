class EmailerAgent:
    def __init__(self, name="Emailer"):
        self.name = name

    def run(self, context):
        """
        Orchestrator-compatible entry point.
        Expects `context` to include:
          - recipient_email
          - github_url
          - overall_score
        """
        recipient_email = context.get("recipient_email", "no-email@example.com")
        github_url = context.get("github_url", "N/A")
        overall_score = context.get("overall_score", 0)

        if overall_score >= 60:
            #print("\n--- EmailerAgent: Preparing Project Analysis Email ---")
            print(f"To: {recipient_email}")
            #print(f"Subject: ScoreInator Project Assessment - {github_url}\n")
            #print(f"Below mentioned project has cleared initial or first level of assessment.")
            #print("Detailed Project analysis details are attached.\n")
            context["email_status"] = "sent"
            return {"status": "success", "recipient": recipient_email}
        else:
            #print(f"\n--- EmailerAgent: Project did not pass initial assessment (Score: {overall_score}) ---")
            context["email_status"] = "not_sent"
            return {"status": "skipped", "recipient": recipient_email, "reason": "Score below 60"}
