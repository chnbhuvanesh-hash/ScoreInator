import requests
from google import adk


@adk.agent()
def validator_agent(context: adk.Context, github_url: str) -> dict:
    """
    Validator Agent.
    Checks whether the provided GitHub URL is valid and accessible.

    Args:
        context (adk.Context): ADK context object.
        github_url (str): GitHub repository URL.

    Returns:
        dict: { "is_valid": bool, "message": str }
    """
    if not github_url.startswith("https://github.com/"):
        return {"is_valid": False, "message": "URL must start with https://github.com/"}

    try:
        response = requests.get(github_url)
        if response.status_code == 200:
            return {"is_valid": True, "message": "GitHub repository is accessible."}
        else:
            return {"is_valid": False, "message": f"Received status code {response.status_code}"}
    except requests.RequestException as e:
        return {"is_valid": False, "message": str(e)}
