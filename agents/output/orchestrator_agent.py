import importlib
import yaml
import os
from datetime import datetime
import json

class OrchestratorAgent:
    def __init__(self, config_file):
        # Load YAML configuration
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)

        self.agents = {}
        self._load_agents()
        self.final_report = {}

    def _load_agents(self):
        """Dynamically load agents from YAML config."""
        agent_definitions = self.config.get('agent_definitions', {})
        for agent_name, details in agent_definitions.items():
            try:
                module_path = details['file'].replace('/', '.').replace('.py', '')
                class_name = details['class']

                module = importlib.import_module(module_path)
                agent_class = getattr(module, class_name)

                # Initialize agent without extra args
                self.agents[agent_name] = agent_class()

            except (ImportError, AttributeError, KeyError) as e:
                print(f"⚠️ Error loading agent '{agent_name}': {e}")

    def _run_pipeline(self, pipeline_config, context):
        """Run each agent in sequence with shared context."""
        for step in pipeline_config:
            agent_name = step['agent']
            agent_instance = self.agents.get(agent_name)

            if not agent_instance:
                print(f"⚠️ Orchestrator: Agent '{agent_name}' not found.")
                continue

            print(f"➡️ Running {agent_name}...")

            try:
                # Call agent's run or run_analysis
                result = {}
                if hasattr(agent_instance, 'run'):
                    result = agent_instance.run(context)
                elif hasattr(agent_instance, 'run_analysis'):
                    result = agent_instance.run_analysis(context.get("github_url"))

                # Ensure 'score' exists
                if result:
                    if "score" not in result and "analysis_score" in result:
                        result["score"] = result["analysis_score"]
                    result["score"] = result.get("score", 0)

                # Store result
                report_key = f"{agent_name}_report"
                self.final_report[report_key] = result
                context[report_key] = result

            except Exception as e:
                print(f"⚠️ Error while running agent '{agent_name}': {e}")
                continue

        return True

    def run_analysis(self, github_url, recipient_email):
        """Run full pipeline, save report, and print summary."""
        print(f"🔍 Starting analysis for: {github_url}\n")

        context = {"github_url": github_url, "recipient_email": recipient_email}
        self.final_report = {}

        # Run pipelines
        core_pipeline = self.config.get('pipeline', [])
        self._run_pipeline(core_pipeline, context)
        special_agents = self.config.get('special_agents', [])
        self._run_pipeline(special_agents, context)
        final_agents = self.config.get('final_step', [])
        self._run_pipeline(final_agents, context)

        # Compute weighted overall score
        agent_weights = {
            "code_scout": 1.0,
            "architect": 1.0,
            "code_quality": 2.0,
            "security_analyst": 2.0,
            "community_manager": 1.0,
            "efficiency_analyst": 1.5,
            "futuristic_analyser": 1.0,
            "ai_contributor": 1.0,
            "pitch_deck_analyst": 0.5
        }

        total_score = 0.0
        total_weight = 0.0
        detailed_results = []

        for agent_key, result in self.final_report.items():
            agent_name = agent_key.replace("_report", "")
            if isinstance(result, dict) and "score" in result:
                weight = agent_weights.get(agent_name, 1.0)
                total_score += result["score"] * weight
                total_weight += weight
            detailed_results.append({agent_name: result})

        overall_score = (total_score / total_weight) if total_weight else 0
        overall_score = round(overall_score, 2)

        # Save detailed report
        os.makedirs("Reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"Reports/final_report_{timestamp}.json"
        with open(report_file, "w") as f:
            json.dump({
                "github_url": github_url,
                "recipient_email": recipient_email,
                "overall_score": overall_score,
                "details": self.final_report
            }, f, indent=4)

        # Console report
        print("\n--- ScoreInator Analysis Report ---\n")
        for agent in detailed_results:
            for name, data in agent.items():
                print(f"--- {name.replace('_',' ').title()} ---")
                if isinstance(data, dict):
                    for k, v in data.items():
                        print(f"{k.replace('_',' ').title()}: {v}")
                print()
        print(f"--- Overall Score: {overall_score}% ---")
        print("=" * 50)

        # Emailer summary
        print()
        if overall_score >= 60:
            print("Below mentioned project has cleared the first level of assessment.")
            print("Detailed project analysis is attached in the report file.\n")
            print("--- EmailerAgent: Email sent successfully ---\n")
            print("✅ ScorInation Bot : Successfully Validated the Provided Hackathon Project.")
        else:
            print("Pass mark is 60%.")
            print("❌ Project did not clear the first level of assessment.")
            print(f"📂 Detailed scorecards are available in file: {report_file}")
            print("📧 Email not sent to the Judge Panel.\n")

        return {
            "success": True,
            "report": self.final_report,
            "overall_score": overall_score,
            "report_file": report_file
        }
