# 🍽️ AI Restaurant Name Generator

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-LLMs-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Cerebras](https://img.shields.io/badge/Cerebras-LLM-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

An **AI-powered web application** that generates **creative and fancy restaurant names** based on cuisine type.  
Built to demonstrate **full-stack AI development skills**, **LLM integration**, and **production-ready deployment** using Docker.

---

## 🚀 Project Overview

Choosing a memorable restaurant name is crucial for branding but often challenging.  
This project automates the process using **Large Language Models (LLMs)** and provides **real-time name generation** through a clean **Streamlit interface**.

**Highlights for recruiters:**

- Full-stack AI application with **Python, Streamlit, LangChain, and Docker**  
- Integrates **Cerebras/OpenAI-compatible LLM** via secure API  
- Demonstrates **production-ready deployment skills**  
- Emphasizes **secure API key management and containerization**

---

## 🧠 Key Features

- 🎯 Generates **one unique restaurant name** per cuisine  
- 🧠 LLM-powered with **LangChain Prompt Templates**  
- ⚡ Integrates with **Cerebras LLM** for fast and reliable output  
- 🎨 Clean **Streamlit UI** for easy user interaction  
- 🔐 API keys securely managed via `.env`  
- 🐳 Fully **Dockerized** for portability and cloud deployment  
- ☁️ Cloud-ready (AWS, Render, Railway)

---

## 🏗️ Tech Stack

 Layer | Technology 
-----|-----------
 Programming Language | Python 3.10 
 LLM Framework | LangChain 
 LLM Provider | Cerebras (OpenAI-compatible API) 
 Frontend UI | Streamlit 
 Environment Management | python-dotenv 
 Containerization | Docker 
 Deployment | Docker Hub, Cloud (Render / AWS / Railway) 

---

## 📂 Project Structure

```text
restaurant_name_generator/
│
├── app.py                   # Streamlit UI for user interaction
├── langchain_helper.py      # LLM logic & LangChain prompt templates
├── requirements.txt         # Python dependencies
├── .env.example             # Template for environment variables
├── screenshots/
│   ├── home.png
│   └── output.png
├── Dockerfile               # Container configuration
└── README.md                # Project documentation
```

## 🔄 Application Workflow

1.User selects a Cuisine
2.Input is sent to LangChain prompt templates
3.LLM generates a creative restaurant name
4.Streamlit UI displays the result instantly

## 🖥️ Application Screenshots
🔹 Home Page

🔹 Generated Restaurant Name

## ⚙️ Run Locally (Without Docker)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Run Using Docker
```bash
Build Docker Image
docker build -t restaurant-ai .
```

## Run Container
``` bash
docker run -p 8501:8501 --env-file .env restaurant-ai
```

## 🌐 Access Application

Streamlit UI → http://localhost:8501

## 🐳 Docker Hub
The application is available as a pre-built Docker image on Docker Hub.

👉 **Docker Hub Repository:**  
https://hub.docker.com/r/aravindvojjala/restaurant-ai

### Pull Image
```bash
docker pull aravindvojjala/restaurant-ai
```

### Run Image
```bash
docker run -p 8000:8000 -p 8501:8501 aravindvojjala/restaurant-ai
```

## Stop container:
```bash
docker ps
docker stop <container_id>
```
