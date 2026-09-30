from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import chatbot, students
from app.core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Student Database Application System",
    description="""
Modular Student Database Backend Application.

Features:
- Student CRUD operations
- SQLite database
- SQLAlchemy ORM
- FastAPI REST APIs
- Swagger API documentation
- Gemini AI chatbot
- LangGraph workflow
- Database-aware AI responses
""",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router, prefix="/api/v1/students", tags=["Students"])
app.include_router(chatbot.router, prefix="/api/v1/chat", tags=["AI Chatbot"])


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Student Database API is running",
        "documentation": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy"}
