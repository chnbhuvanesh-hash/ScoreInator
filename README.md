# 🎯 Score-Inator

**Score-Inator** is an AI-powered **hackathon project evaluation system** built using the **Google ADK (Agent Development Kit)**.  
It uses multiple specialized agents (bots) to analyze GitHub-hosted projects and generate a **comprehensive assessment report**.  

The tool helps hackathon judges and mentors **automate initial screening**, evaluating code quality, architecture, security, community activity, presentation readiness, and future innovation.  

---

## 🚀 Features

- **Multi-Agent Evaluation** – Each agent evaluates one dimension of the project:
  - **Core Agents**
    - `CodeScoutAgent` – Detects project structure, files, and completeness.
    - `ArchitectAgent` – Evaluates modularity, scalability, and architecture.
    - `EfficiencyAnalystAgent` – Looks for efficiency and performance optimizations.
  - **Analyzer Agents**
    - `CodeQualityAgent` – Checks linting errors, test coverage, and maintainability.
    - `SecurityAnalystAgent` – Identifies vulnerabilities or security flaws.
    - `CommunityManagerAgent` – Evaluates README, docs, and collaboration potential.
  - **Wow Agents**
    - `AIContributorAgent` – Suggests AI/automation improvements.
    - `FuturisticAnalyserAgent` – Assesses innovation and forward-thinking aspects.
    - `PitchDeckAnalystAgent` – Reviews presentation clarity and storytelling.
  - **Output Agents**
    - `OrchestratorAgent` – Runs the pipeline and aggregates reports.
    - `EmailerAgent` – Sends notifications to the judging panel.

- **Threshold-Based Pass/Fail System** –  
  Projects must score at least **60% overall** to clear the **first-level assessment**.

- **Detailed Reports** –  
  All results are saved in the `Reports/` folder as JSON files for later review.

- **Judge Notifications** –  
  If a project passes, an email is automatically sent to the judging panel.

---

## 📂 Project Structure

ScoreInator/
│── agents/
│ ├── init.py
│ ├── analyzer/
│ │ ├── code_quality_agent.py
│ │ ├── security_analyst_agent.py
│ │ └── community_manager_agent.py
│ ├── core/
│ │ ├── code_scout_agent.py
│ │ ├── architect_agent.py
│ │ └── efficiency_analyst_agent.py
│ ├── output/
│ │ ├── orchestrator_agent.py
│ │ └── emailer_agent.py
│ ├── wow/
│ │ ├── ai_contributor_agent.py
│ │ ├── futuristic_analyser_agent.py
│ │ └── pitch_deck_analyst_agent.py
│
│── tools/
│ ├── init.py
│ ├── github_tools.py # Existing GitHub metadata utilities
│ ├── security_tools.py # For vulnerability checks
│ ├── llm_tools.py # For AI/LLM-based code suggestions
│ ├── presentation_tools.py # For PPT/video analysis
│
│── main.py # Entry point
│── orchestrator_config.yaml # Configuration for the Orchestrator
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── LICENSE # License file


---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/score-inator.git
   cd score-inator

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python main.py

▶️ Usage

When you run main.py, you will be prompted for:

GitHub project URL

Recipient email address

After analysis:

Reports are saved in the Reports/ folder.

If the project passes (≥ 60%), an email is sent to the judging pane

🧪 Sample Test Results
❌ Example 1 – Project Fails Assessment

Please enter the GitHub URL to analyze: https://github.com/TheOdinProject/javascript-exercises
Please enter the recipient email address: chnbhuvanesh@gmail.com
🔍 Starting analysis for: https://github.com/TheOdinProject/javascript-exercises

➡️ Running code_scout...
➡️ Running architect...
➡️ Running code_quality...
➡️ Running security_analyst...
➡️ Running community_manager...
➡️ Running efficiency_analyst...
➡️ Running futuristic_analyser...
➡️ Running ai_contributor...
➡️ Running pitch_deck_analyst...
➡️ Running orchestrator...
➡️ Running emailer...

--- EmailerAgent: Project did not pass initial assessment ---
ℹ️ Pass mark is 60%.
📂 Detailed scorecards are available in file: Reports/final_report.json

--- ScoreInator Analysis Report ---

--- Overall Score: 57 ---
==================================================

❌ Project did not clear the first level of assessment.
📧 Email not sent to the Judge Panel.


✅ Example 2 – Project Passes Assessment

Please enter the GitHub URL to analyze: https://github.com/sample/hackathon-ai-project
Please enter the recipient email address: chnbhuvanesh@gmail.com
🔍 Starting analysis for: https://github.com/sample/hackathon-ai-project

➡️ Running code_scout...
➡️ Running architect...
➡️ Running code_quality...
➡️ Running security_analyst...
➡️ Running community_manager...
➡️ Running efficiency_analyst...
➡️ Running futuristic_analyser...
➡️ Running ai_contributor...
➡️ Running pitch_deck_analyst...
➡️ Running orchestrator...
➡️ Running emailer...

Below mentioned project has cleared the first level of assessment.
Detailed project analysis is attached in the report file.

--- EmailerAgent: Email sent successfully ---

✅ ScoreInator Bot: Successfully validated the provided hackathon project.

--- ScoreInator Analysis Report ---

--- Overall Score: 63.73 ---
==================================================

✅ Project passed the first level of assessment.
ℹ️ Pass mark is 60%.
📂 Detailed scorecards are available in file: Reports/final_report.json
📧 Email has been sent to the Judge Panel.


🛠 Future Enhancements

Integrate SonarQube or Bandit for real static/security analysis.

Add GitHub Actions for CI/CD automated evaluations.

Support multiple output formats (PDF, HTML).

Enable Slack/Teams integration for judge notifications.

👨‍💻 Contributors

[THe ScoreKeepers : Google Agentic AI Hackathon]

Bhuvanesh Balaji – Project Owner & Developer

Manimaran Govindarajan - Project Owner & Developer

Score-Inator Agents – AI-based hackathon evaluators

