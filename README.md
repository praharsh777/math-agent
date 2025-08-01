# 📐 Math Routing Agent (RAG-Style FastAPI Project)

This project is a **FastAPI-based intelligent math question-answering system**. It uses a hybrid approach of a semantic **Knowledge Base (FAISS)** and a **Wikipedia fallback** to answer user queries accurately — inspired by the concept of Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 🔍 FAISS-powered vector similarity search over predefined Q&A (`kb.json`)
- 🧠 Smart routing logic: Use KB if match is confident, else fallback to Wikipedia
- 🌐 FastAPI endpoints with Swagger Docs (`/docs`)
- 📖 Wikipedia integration using LangChain Tools
- ✅ Built-in benchmarking and feedback logging system (optional)

---

## 🧠 Tech Stack

- **FastAPI** – for API routes
- **FAISS** – for semantic search over math knowledge base
- **LangChain** – for Wikipedia integration
- **HuggingFace Transformers** – for sentence embeddings
- **Pydantic** – for request/response modeling

---
## 📁 Project Structure

math-agent/
│
├── backend/                           # Main application backend
│   │
│   ├── main.py                        # FastAPI entry point
│   │
│   ├── agents/                        # Agent logic for routing
│   │   └── router.py                  # Routes question to KB or Wikipedia
│   │
│   ├── services/                      # Core services
│   │   ├── vectorstore.py             # FAISS-based KB embedding and querying
│   │   ├── benchmark.py               # Optional: accuracy evaluation module
│   │   └── feedback.py                # Feedback logging support
│   │
│   ├── tools/                         # External tool integrations
│   │   └── wiki_tool.py               # Wikipedia search fallback via LangChain
│   │
│   ├── data/                          # Data files
│   │   └── kb.json                    # Static math Q&A dataset
│   │
│   └── requirements.txt              # Python dependencies
│
└── README.md                         # Project documentation

---
## 🧪 How to Run Locally

### 1. Clone the Repo
git clone https://github.com/praharsh777/math-agent.git
cd math-agent/backend
2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate
3. Install Requirements

pip install -r requirements.txt
4. Run the Server

uvicorn main:app --reload --host 0.0.0.0 --port 8000
5. Open Swagger Docs
Navigate to:


http://localhost:8000/docs
Or in Codespaces:


https://<your-codespace-url>.github.dev/docs
🧭 API Usage
GET /ask?q=your_question
Example:

GET /ask?q=What is the derivative of x^2?
Response:

{
  "question": "What is the derivative of x^2?",
  "answer": "The derivative of x² is 2x.",
  "score": 1,
  "matched_question": "What is the derivative of x^2?",
  "source": "Knowledge Base"
}
📌 Notes
.venv is excluded from Git to avoid uploading large Python environments.

FAISS vectors are generated in-memory during app startup.

Wikipedia fallback ensures graceful handling of unseen questions.

📽 Demo
Watch the demo video : [Link](https://youtu.be/uOV8dI7-VKs?si=NTDSrU5m-rtsyrxW)

📄 License
This project is built for educational and evaluation purposes.


