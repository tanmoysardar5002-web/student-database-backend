# Student Database Application System

A modular backend application for managing student records using FastAPI, SQLite and SQLAlchemy.

It also includes a basic AI chatbot powered by Google's Gemini API and LangGraph. The chatbot reads the current student records from SQLite and answers questions about them.

## Technologies

- Python 3.12+
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Google Gemini API
- LangGraph
- Uvicorn
- Docker

## Features

- Create student
- Get all students
- Get one student
- Update student
- Delete student
- Search students
- Gemini database-aware chatbot
- LangGraph workflow
- Automatic Swagger documentation
- Docker support

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini

Copy `.env.example` to `.env` and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-2.5-flash
DATABASE_URL=sqlite:///./data/students.db
```

Never commit `.env` to GitHub.

### 4. Add sample students

```bash
python seed.py
```

### 5. Start the backend

```bash
python run.py
```

Backend:

`http://127.0.0.1:8000`

Swagger:

`http://127.0.0.1:8000/docs`

ReDoc:

`http://127.0.0.1:8000/redoc`

## API Endpoints

### Students

```text
POST   /api/v1/students/
GET    /api/v1/students/
GET    /api/v1/students/search?q=BCA
GET    /api/v1/students/{student_id}
PUT    /api/v1/students/{student_id}
DELETE /api/v1/students/{student_id}
```

### AI Chatbot

```text
POST /api/v1/chat/
```

Example:

```json
{
  "question": "Who has the highest CGPA?"
}
```

Other examples:

```text
Which students are in semester 4?
What is Priya's CGPA?
How many students are studying BCA?
Which student has a CGPA above 8.5?
```

## Architecture

```text
Client
  |
  v
FastAPI
  |
  +--------------------+
  |                    |
  v                    v
Student APIs        Chat API
  |                    |
  v                    v
Service Layer       LangGraph
  |                    |
  v                    v
SQLAlchemy          Gemini API
  |
  v
SQLite
```

## LangGraph Flow

```text
User Question
      |
      v
Chat API
      |
      v
Read SQLite Database
      |
      v
Build Database Context
      |
      v
LangGraph
      |
      v
Gemini
      |
      v
Answer
```

## Docker

Create `.env`, then run:

```bash
docker compose up --build
```

Swagger:

`http://localhost:8000/docs`

## Security Note

This project is intended as a student/portfolio backend. For production use, add authentication, authorization, rate limiting, stricter CORS settings, secret management, database migrations, and more granular AI data access.
