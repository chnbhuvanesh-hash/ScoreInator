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
        # Aggregate real scores from each agent if present
        total_score = 0
        count = 0
        for r in self.reports:
            result = r.get("result", {})
            score = result.get("score")
            if score is not None:
                total_score += score
                count += 1

        final_score = round(total_score / count) if count > 0 else 0

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
