# 🍽️ AI Restaurant Name Generator

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-LLMs-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Cerebras](https://img.shields.io/badge/Cerebras-LLM-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

An **AI-powered web application** that generates **exactly ONE fancy restaurant name** based on a selected cuisine using **LangChain** and **Large Language Models (LLMs)**, delivered through an interactive **Streamlit UI**.

---

## 🚀 Project Overview

Choosing a perfect restaurant name is often challenging and time-consuming.  
This project provides an **AI-driven solution** that instantly generates **creative and fancy restaurant names** tailored to a specific cuisine.

The application is designed to be:

- ✅ Simple  
- ✅ Secure  
- ✅ Scalable  
- ✅ Docker & Cloud ready  

---

## 🧠 Key Features

- 🍽️ Cuisine-based restaurant name generation  
- 🧠 Powered by **LangChain Prompt Templates**
- ⚡ Uses **Cerebras (OpenAI-compatible) LLM API**
- 🎨 Clean and interactive **Streamlit Web UI**
- 🔐 Secure API key management using `.env`
- 🐳 Fully Dockerized
- ☁️ Ready for Cloud deployment (AWS / Render / Railway)

---

## 🏗️ Tech Stack

| Layer | Technology |
|-----|-----------
| Programming Language | Python 3.10 
| LLM Framework | LangChain 
| LLM Provider | Cerebras (OpenAI-compatible API) 
| Frontend UI | Streamlit 
 Environment Management | python-dotenv 
 Containerization | Docker 
 Deployment | Docker Hub 

---

## 📂 Project Structure

```text
restaurant_name_generator/
│
├── app.py                   # Streamlit frontend
├── langchain_helper.py      # LangChain & LLM logic
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
├── screenshots/
│   ├── home.png
│   └── output.png
├── Dockerfile
└── README.md
```
