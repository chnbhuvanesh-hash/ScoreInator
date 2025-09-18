import json
import os
from datetime import datetime

class ReporterAgent:
    def __init__(self):
        self.reports = []

    def collect_report(self, agent_name, result):
        """Collect results from each agent in the pipeline."""
        self.reports.append({
            "agent": agent_name,
            "result": result
        })

    def run(self, inputs=None):
        """
        Finalize the report by aggregating all collected agent outputs.
        Returns a dictionary with the final score and details.
        """
        # Example scoring (replace with your real logic)
        final_score = sum(i for i in range(len(self.reports))) * 10  

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "final_score": final_score,
            "details": self.reports
        }

        # Save as JSON
        os.makedirs("reports", exist_ok=True)
        report_file = f"reports/final_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as f:
            json.dump(report, f, indent=4)

        return report
