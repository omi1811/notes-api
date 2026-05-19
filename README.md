# 📝 Notes API + Dashboard

A full-stack CRUD application built with FastAPI (backend) and Streamlit (frontend).  

## ️ Tech Stack
- **Backend**: FastAPI, Pydantic, Uvicorn, CORS
- **Frontend**: Streamlit, Requests

- **Architecture**: REST API + Stateless Frontend

## 🚀 Local Setup
```bash
# Backend
pip install -r requirements.txt
uvicorn src.main:app --reload

# Frontend (new terminal)
streamlit run frontend/app.py
