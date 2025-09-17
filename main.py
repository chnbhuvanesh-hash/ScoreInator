# score-inator/main.py
"""
Score-inator Agentic Bot - entrypoint

This file:
- Exposes `root_agent` (simple wrapper) so ADK can detect a root agent if ADK inspects symbols.
- Provides a standalone CLI to run the agent flow:
    python main.py https://github.com/owner/repo
"""

import sys
import argparse
import os
from dotenv import load_dotenv

# Load .env if present (for optional GITHUB_TOKEN)
load_dotenv()

from agents.coordinator_agent import CoordinatorAgent

# Create a simple root_agent object so ADK loader (if it inspects this module)
# can find a symbol named `root_agent`. ADK often expects an Agent-like object.
# Here it's a thin wrapper around CoordinatorAgent for compatibility.
class RootAgentWrapper:
    def __init__(self):
        self.name = "score-inator"
        self.description = "Coordinator for Score-inator: validates, analyzes and scores GitHub projects."
        self.coordinator = CoordinatorAgent()

    def run(self, args):
        # Accept a single GitHub URL or read from args
        return self.coordinator.run(args)

# Expose variable for ADK to discover
root_agent = RootAgentWrapper()


def cli_main():
    parser = argparse.ArgumentParser(description="Score-inator Agentic Bot - validate, analyze and score GitHub projects.")
    parser.add_argument("github_url", type=str, help="Public GitHub repository URL (example: https://github.com/owner/repo)")
    parser.add_argument("--token", type=str, default=os.getenv("GITHUB_TOKEN"), help="Optional GitHub token (or set GITHUB_TOKEN in .env)")
    parser.add_argument("--save", type=str, default=None, help="Optional path to save JSON summary")
    args = parser.parse_args()
    result = root_agent.run(vars(args))
    # Print prettified result
    print("\n" + "="*80)
    print("SCORE-INATOR RESULT")
    print("="*80)
    print("Project Summary:\n")
    print(result["summary"])
    print("\nScore (1-10):", result["score"])
    print("\nScoring breakdown:")
    for k, v in result["breakdown"].items():
        print(f" - {k}: {v}")
    if args.save:
        import json
        with open(args.save, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print(f"\nSaved output to {args.save}")
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python main.py <github_url> [--token TOKEN] [--save out.json]")
        sys.exit(1)
    cli_main()
