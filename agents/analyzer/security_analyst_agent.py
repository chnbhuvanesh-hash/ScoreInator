import random

class SecurityAnalystAgent:
    def __init__(self, name="Security Analyst"):
        self.name = name

    def run(self, context: dict):
        """Standard entry point for orchestrator"""
        github_url = context.get("github_url")
        return self.run_analysis(github_url)

    def run_analysis(self, github_url: str):
        """
        Fake but realistic security scan simulation.
        In production: integrate with tools like Bandit, Safety, Trivy, etc.
        """
        # Simulate dependency scan
        dependencies_checked = random.randint(10, 100)

        # Random vulnerabilities found
        vulnerabilities_found = random.randint(0, 5)

        # Risk scoring
        vuln_penalty = vulnerabilities_found * 15
        dependency_health = max(0, 100 - (dependencies_checked // 5))

        # Weighted scoring
        final_score = round((100 - vuln_penalty) * 0.7 + dependency_health * 0.3, 2)
        final_score = max(0, min(100, final_score))  # clamp to 0-100

        return {
            "valid": True,
            "dependencies_checked": dependencies_checked,
            "vulnerabilities_found": vulnerabilities_found,
            "score": final_score
        }
