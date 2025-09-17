# Score-Inator 🎯

Score-Inator is a hackathon project built with the **Google Agent Development Kit (ADK)**.  
It is a simple but powerful scoring assistant agent that responds to user queries with concise scores and explanations.

---

## 🚀 Features
- Built with **Google ADK v1.x**
- Uses **Gemini-1.5-Flash** as the LLM
- Provides concise scoring responses
- Designed to demonstrate **multi-agent workflows** in a hackathon setting
- Loads secrets via `.env` file for safe API key management

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/score-inator.git
cd score-inator

2. Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_api_key_here


⚠️ Do not commit .env to GitHub!
Add .env to .gitignore to keep your secrets safe.

5. Run the Agent
adk run

📂 Project Structure
score-inator/
│── agents/           # Agent definitions
│── tools/            # Tools used by agents
│── main.py           # Entry point
│── root_agent.yaml   # Root agent configuration
│── requirements.txt  # Python dependencies
│── README.md         # Project documentation
│── LICENSE           # License file

🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.