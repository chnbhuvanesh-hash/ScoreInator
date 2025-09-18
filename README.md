# Score-Inator 🎯

Score-Inator is a hackathon project built with the **Google Agent Development Kit (ADK)**.  
It is a simple but powerful scoring assistant agent that responds to user queries with concise scores and explanations.  
Originally created for the **Google Agentic AI Hackathon**.

---

## 🚀 Features
- Built with **Google ADK v1.x**
- Uses **Gemini-1.5-Flash** as the LLM
- Provides concise scoring responses
- Demonstrates **multi-agent workflows**
- Loads secrets via `.env` file for safe API key management

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/chnbhuvanesh-hash/ScoreInator.git
cd ScoreInator
2. Create & Activate Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root:

env
Copy code
GOOGLE_API_KEY=your_api_key_here
⚠️ Do not commit .env to GitHub!
Ensure .env is listed in .gitignore.

5. Run the Agent
bash
Copy code
adk run
📂 Project Structure
bash
Copy code
ScoreInator/
│── agents/analyzer_agent.py
│── agents/coordinator_agent.py
│── agents/validator_agent.py   # Agent definitions
│── tools/github_tools.py          # Tools used by agents
│── main.py           # Entry point
│── root_agent.yaml   # Root agent configuration
│── requirements.txt  # Python dependencies
│── README.md         # Project documentation
│── LICENSE           # License file
🤝 Contributing
Contributions are welcome!
Please fork the repo and submit a pull request.

yaml
Copy code

---

### 🔧 Next Steps
1. Replace your current `README.md` with the above.  
2. Stage & commit the fix:
   ```bash
   git add README.md
   git commit -m "Resolved merge conflict and cleaned up README.md"
   git push -u origin main