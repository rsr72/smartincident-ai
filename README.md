# SmartIncident-AI

An AI-powered incident assistant that summarizes logs, identifies root causes, and suggests fixes using OpenAI's GPT-3.5 or GPT-4 API.

## 🚀 Features

- REST endpoint to analyze system or CI/CD logs
- Intelligent summaries with root cause analysis and resolution guidance
- Designed for cloud-native deployment (AWS Lambda or Azure Functions)
- GitHub Actions for CI/CD automation
- Modular structure with support for future Ansible integration and visualization


---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Pydantic, Uvicorn
- **AI:** OpenAI GPT-4 API
- **Environment:** dotenv for local secret management
- **CI/CD:** GitHub Actions
- **Deployment (Optional):** AWS Lambda, Azure Functions
- **Testing:** Pytest (planned)
- **Infra as Code (Planned):** Terraform or Bicep
- **Logging:** JSON or SQLite (MVP), CockroachDB/MySQL (future)

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/smartincident-ai.git
cd smartincident-ai
