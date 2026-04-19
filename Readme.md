# Aptiva
# 🚀 Aptiva — AI Job Application Agent

> Your intelligent co-pilot for discovering, tailoring, and applying to jobs — automatically.

---

## 🧠 What is Aptiva?

**Aptiva** is an AI-powered job application system that helps you:

* 🔍 Discover relevant job opportunities
* ✍️ Generate tailored resumes & cover letters
* 🤖 Automatically apply to jobs (agent-based workflows)
* 📊 Track applications and optimize success rates

Think of it as your **24/7 job-hunting AI agent**.

---

## ⚡ Core Features

### 🤖 AI Job Agent

* Autonomous workflows for job discovery and applications
* Smart filtering based on skills, preferences, and history

### 📝 Resume & Cover Letter Generation

* Context-aware resume tailoring
* AI-generated cover letters per job description

### 🔗 Platform Integration

* Designed for platforms like LinkedIn (extensible)
* Modular automation layer

### 📊 Application Tracking

* Track status, responses, and performance
* Improve strategy using insights

---

## 🏗️ Tech Stack

### Frontend

* React (Vite)
* TailwindCSS

### Backend

* FastAPI
* SQLAlchemy
* Alembic (migrations)

### AI Layer

* LLM-powered agents
* Vector database (pluggable: FAISS / alternatives)

---

## 📁 Project Structure

```bash
ai-job-agent/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── services/
│   ├── hooks/
│   └── utils/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   └── services/
│   ├── alembic/
│   └── db/
│
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/aptiva.git
cd aptiva
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

Run migrations:

```bash
alembic upgrade head
```

Start server:

```bash
uvicorn app.main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🔐 Environment Variables

Create a `.env` file in `backend/`:

```env
DATABASE_URL=sqlite:///./ai_job_agent.db
OPENAI_API_KEY=your_key_here
```

---

## 🧩 Roadmap

* [ ] LinkedIn auto-apply agent
* [ ] Resume optimization scoring
* [ ] Multi-platform job scraping
* [ ] AI interview preparation module
* [ ] Analytics dashboard

---

## ⚠️ Disclaimer

This project is for **educational and research purposes**.
Use automation responsibly and in accordance with platform policies.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## ⭐ Support

If you find this useful, consider giving it a star ⭐

---

## 🧬 Vision

Aptiva aims to become a **fully autonomous career agent** —
handling everything from job discovery to offer negotiation.

---
