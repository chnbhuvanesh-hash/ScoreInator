import importlib
import yaml
from datetime import datetime

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
                # Call agent's run or run_analysis if present
                if hasattr(agent_instance, 'run'):
                    result = agent_instance.run(context)
                elif hasattr(agent_instance, 'run_analysis'):
                    result = agent_instance.run_analysis(context.get("github_url"))
                else:
                    result = {}

                # Store result in context and final_report
                report_key = f"{agent_name}_report"
                self.final_report[report_key] = result
                context[report_key] = result

                # Stop pipeline on failure if configured
                if 'on_failure' in step and not result.get('valid', True):
                    print(f"❌ Orchestrator: {agent_name} failed. Stopping pipeline.")
                    return False

            except Exception as e:
                print(f"⚠️ Error while running agent '{agent_name}': {e}")
                continue  # Continue with other agents

        return True

    def run_analysis(self, github_url, recipient_email):
        """Run full pipeline and build a final report compatible with EmailerAgent."""
        print(f"🔍 Starting analysis for: {github_url}\n")

        context = {
            "github_url": github_url,
            "recipient_email": recipient_email,
        }

        self.final_report = {}

        # Run core pipeline
        core_pipeline = self.config.get('pipeline', [])
        self._run_pipeline(core_pipeline, context)

        # Run special agents
        special_agents = self.config.get('special_agents', [])
        self._run_pipeline(special_agents, context)

        # Run final step (reporter + emailer)
        final_agents = self.config.get('final_step', [])
        self._run_pipeline(final_agents, context)

        # -------------------------------
        # Prepare final_report for EmailerAgent
        # -------------------------------
        overall_score = 0
        scored_agents = 0
        detailed_results = []

        for agent_key, result in self.final_report.items():
            agent_name = agent_key.replace("_report", "").replace("_", " ").title()
            if isinstance(result, dict) and "score" in result:
                overall_score += result["score"]
                scored_agents += 1
            detailed_results.append({agent_name: result})

        overall_score = overall_score // scored_agents if scored_agents else 0

        # Include reporter summary
        self.final_report["reporter_report"] = {
            "timestamp": datetime.now().isoformat(),
            "final_score": overall_score,
            "details": detailed_results
        }

        # Include emailer status placeholder
        self.final_report["emailer_report"] = {
            "status": "pending",
            "recipient": recipient_email
        }

        # -------------------------------
        # Print nicely formatted console report
        # -------------------------------
        print("\n--- ScoreInator Analysis Report ---\n")
        for agent in detailed_results:
            for name, data in agent.items():
                print(f"--- {name} ---")
                if isinstance(data, dict):
                    for k, v in data.items():
                        print(f"{k.replace('_',' ').title()}: {v}")
                print()
        print(f"--- Overall Score: {overall_score} ---")
        print("="*50)

        # -------------------------------
        # Simulate EmailerAgent sending email
        # -------------------------------
        print("\n--- EmailerAgent: Preparing Project Analysis Email ---")
        print(f"To: {recipient_email}")
        print(f"Subject: ScoreInator Analysis Report for {github_url}\n")
        print(f"Project URL: {github_url}")
        print(f"Overall Score: {overall_score}\n")
        print("--- Detailed Agent Results ---\n")
        for agent in detailed_results:
            for name, data in agent.items():
                print(f"--- {name} ---")
                if isinstance(data, dict):
                    for k, v in data.items():
                        print(f"{k.replace('_',' ').title()}: {v}")
                print()
        print("--- EmailerAgent: Email sent successfully ---\n")

        print("✅ Orchestrator: Analysis complete.")

        return {"success": True, "report": self.final_report, "overall_score": overall_score}
