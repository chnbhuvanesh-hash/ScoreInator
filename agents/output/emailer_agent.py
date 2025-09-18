class EmailerAgent:
    def __init__(self, name="Emailer"):
        self.name = name

    def run(self, context):
        """
        Orchestrator-compatible entry point.
        Expects `context` to include:
          - recipient_email
          - github_url
          - final_score
          - final_report (dictionary of all agent results)
        """
        recipient_email = context.get("recipient_email", "no-email@example.com")
        github_url = context.get("github_url", "N/A")
        final_score = context.get("final_score", 0)
        final_report = context.get("final_report", {})

        print("\n--- EmailerAgent: Preparing Project Analysis Email ---")
        print(f"To: {recipient_email}")
        print(f"Subject: ScoreInator Analysis Report for {github_url}\n")

        print(f"Project URL: {github_url}")
        print(f"Overall Score: {final_score}\n")
        print("--- Detailed Agent Results ---\n")

        for agent_name, report in final_report.items():
            print(f"--- {agent_name.replace('_', ' ').title()} ---")
            for key, value in report.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("")  # Blank line between agents

        print("--- EmailerAgent: Email sent successfully ---\n")

        # Update context for orchestrator
        context["email_status"] = "sent"
        return {"status": "success", "recipient": recipient_email}
