from google import adk
from agents.validator_agent import validator_agent
from agents.analyzer_agent import analyzer_agent
from google.adk import Agent, Context

@adk.agent()
#@Agent(name="coordinator_agent")
def coordinator_agent(context: adk.Context, github_url: str) -> str:
    """
    Coordinator Agent for Score-inator.
    Orchestrates validation, analysis, and scoring of a hackathon project.
    
    Args:
        context (adk.Context): Context object provided by ADK runtime.
        github_url (str): Public GitHub repository URL submitted by user.

    Returns:
        str: Final human-readable summary and score.
    """

    # Step 1: Validate GitHub URL
    validation_result = validator_agent(context, github_url)
    if not validation_result.get("is_valid", False):
        return f"❌ Invalid or inaccessible GitHub URL: {github_url}"

    # Step 2: Analyze README.md & Score project
    analysis_result = analyzer_agent(context, github_url)

    summary = analysis_result.get("summary", "No summary available.")
    score = analysis_result.get("score", "N/A")

    # Step 3: Return formatted output
    return (
        f"✅ Repository analyzed successfully!\n\n"
        f"📄 Summary:\n{summary}\n\n"
        f"🏆 Final Score: {score}/10"
    )
