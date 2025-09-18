import sys
import os
import traceback
from dotenv import load_dotenv
from agents.output.orchestrator_agent import OrchestratorAgent

if __name__ == "__main__":
    # Load environment variables from the .env file
    load_dotenv()

    try:
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
        print("Analysis finished with result:", result)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
