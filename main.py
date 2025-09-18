import sys
import os
import traceback
from dotenv import load_dotenv
from agents.output.orchestrator_agent import OrchestratorAgent


def run_once():
    """Run one project validation cycle."""
    # Prompt the user for the GitHub URL
    github_url = input("Please enter the GitHub URL to analyze: ").strip()
    if not github_url:
        print("Error: GitHub URL cannot be empty.")
        sys.exit(1)

    # Prompt the user for the recipient email
    recipient_email = input("Please enter the recipient email address: ").strip()
    if not recipient_email:
        print("Error: Recipient email cannot be empty.")
        sys.exit(1)

    # Resolve config file path safely
    config_path = os.path.join(os.path.dirname(__file__), "root_agent.yaml")
    if not os.path.exists(config_path):
        print("Error: 'root_agent.yaml' file not found in project root.")
        sys.exit(1)

    # Initialize OrchestratorAgent with config file
    orchestrator = OrchestratorAgent(config_path)

    # Run the analysis
    result = orchestrator.run_analysis(github_url, recipient_email)

    # --- Post-analysis enhancements ---
    if result:
        overall_score = result.get("overall_score", 0)
        log_file = result.get("log_file", "Reports/final_report.json")

        print("\n--- ScoreInator Analysis Report ---\n")
        print(f"--- Overall Score: {overall_score} ---")
        print("==================================================\n")

        if overall_score < 60:
            print("❌ Project did not clear the first level of assessment.")
            print("ℹ️ Pass mark is 60%.")
            print(f"📂 Detailed scorecards are available in file: {log_file}")
            print("📧 Email not sent to the Judge Panel.\n")
        else:
            print("✅ Project passed the first level of assessment.")
            print("ℹ️ Pass mark is 60%.")
            print(f"📂 Detailed scorecards are available in file: {log_file}")
            print("📧 Email has been sent to the Judge Panel.\n")


if __name__ == "__main__":
    # Load environment variables from the .env file
    load_dotenv()

    try:
        while True:
            run_once()
            choice = input("Do you want to validate one more project? (y/n): ").strip().lower()
            if choice != "y":
                print("👋 Exiting ScoreInator. Goodbye!")
                break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
