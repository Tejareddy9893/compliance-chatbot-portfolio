# 🛡️ AI Compliance Risk Monitor
**Real-Time GRC Assistant with Semantic Search, ServiceNow Simulation, and Power BI Analytics**

This project tackles a real-world challenge in governance, risk, and compliance (GRC): monitoring AI-driven risks across hybrid cloud environments. It combines semantic search, risk scoring, and dashboarding to simulate enterprise-grade compliance workflows.

---

## 🚀 Features

- 🔍 **Semantic Search**  
  Embedding-based matching for HIPAA/SOC2 questions using SentenceTransformers + FAISS

- 🧠 **Risk Scoring Engine**  
  Detects high-risk queries (e.g., bias, breach, transfer) and assigns dynamic scores

- 🛠️ **ServiceNow Simulation**  
  Creates mock tickets and retrieves KB articles based on query context

- 📊 **Power BI Dashboard**  
  Visualizes real-time compliance events, risk trends, and ticket activity

- 🗂️ **Modular Architecture**  
  Clean separation of UI, logic, and mock APIs for scalability

---

## 🧠 Tech Stack

| Layer        | Tools Used                                      |
|--------------|--------------------------------------------------|
| UI           | Streamlit                                       |
| NLP          | SentenceTransformers (`all-MiniLM-L6-v2`)       |
| Search       | FAISS                                            |
| Backend      | Python, Pandas                                   |
| Simulation   | Mock ServiceNow API                              |
| Analytics    | Power BI                                         |

---

## 📁 Folder Structure
compliance-risk-monitor/ ├── app/               # Streamlit UI + logic │   ├── main.py │   ├── semantic.py │   ├── risk_engine.py │   └── logger.py ├── service_now/       # Mock ServiceNow API │   ├── init.py │   └── mock_api.py ├── data/              # FAQ, risk logs, chatbot logs │   ├── hipaa_faq.csv │   ├── ai_risk_log.csv │   └── compliance_logs.csv ├── powerbi/           # Dashboard file (.pbix) ├── requirements.txt   # Python dependencies

---

## 🧪 Demo Queries

Try these in the chatbot:
- “What is HIPAA?”
- “Report a HIPAA breach”
- “SOC2 controls article”
- “Create a compliance incident”
- “Flag model bias in EU”

---

## 📊 Dashboard Preview

![Dashboard Screenshot](link-to-screenshot.png)

Or [View Live Dashboard](https://app.powerbi.com/links/YOUR_DASHBOARD_LINK)

---

## ⚙️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/compliance-risk-monitor.git
cd compliance-risk-monitor

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
streamlit run app/main.py



🧭 Future Enhancements
- 🔗 Real ServiceNow API integration
- 🌍 Cross-border compliance logic (GDPR, HIPAA, etc.)
- 📈 Live data streaming via Azure Monitor or AWS CloudWatch
- 🧠 LLM-based policy summarization
- 🧮 Power BI integration with real-time data sources

🙋 About the Author
Built by Saiteja, Strategic Data Consultant & BI Specialist with expertise in GRC, healthcare analytics, and AI/ML integration. Passionate about building enterprise-grade solutions that blend compliance, intelligence, and impact.


---

Let me know when you’re ready for your LinkedIn post — I’ll help you write a high-impact announcement that showcases this project to recruiters and peers. You're building a portfolio that truly stands out!




<img width="1525" height="678" alt="image" src="https://github.com/user-attachments/assets/7b5904e1-d672-4c46-8cc8-62ca4cb9a231" />
