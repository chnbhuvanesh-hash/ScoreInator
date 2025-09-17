# score-inator/main.py
"""
Score-inator Agentic Bot - entrypoint
Handles multiple GitHub repo submissions in one session.
"""

import sys
import os
from dotenv import load_dotenv
from agents.coordinator_agent import CoordinatorAgent

# Load .env if present
load_dotenv()

# Root agent wrapper
class RootAgentWrapper:
    def __init__(self):
        self.name = "score-inator"
        self.description = "Coordinator for Score-inator: validates, analyzes and scores GitHub projects."
        self.coordinator = CoordinatorAgent()

    def run(self, github_url):
        # Accept a single GitHub URL
        return self.coordinator.run({"github_url": github_url})

root_agent = RootAgentWrapper()

def cli_main():
    print("\n🎯 Welcome to Score-inator! Evaluate GitHub projects and get scores.\n")
    
    while True:
        github_url = input("[🚀 GitHub URL] → ").strip()
        if github_url.lower() in {"exit", "quit"}:
            print("\n👋 Exiting Score-inator. Goodbye!")
            break

        # Run the agent
        result = root_agent.run(github_url)

        # Display results
        print("\n" + "="*80)
        print("📊 SCORE-INATOR RESULT")
        print("="*80)
        print("Project Summary:\n")
        print(result["summary"])
        print("\nScoring Breakdown:")
        for k, v in result["breakdown"].items():
            print(f" - {k}: {v}")
        print(f"\n🎯 Final Score → {result['score']}")
        print("="*80)

        # Ask if user wants to continue
        continue_choice = input("\n[🔄 Evaluate another project? yes/no] → ").strip().lower()
        if continue_choice not in {"yes", "y"}:
            print("\n👋 Session closed. Thanks for using Score-inator!")
            break

if __name__ == "__main__":
    cli_main()
