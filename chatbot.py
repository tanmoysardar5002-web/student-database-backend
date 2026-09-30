import json

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.ai.graph import chat_graph
from app.core.database import get_db
from app.services.student_service import get_database_context

router = APIRouter()


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=1000)


class ChatResponse(BaseModel):
    question: str
    answer: str


@router.post("/", response_model=ChatResponse, summary="Ask the student database AI assistant")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    students = get_database_context(db)
    database_context = json.dumps(students, indent=2)

    result = chat_graph.invoke(
        {
            "question": request.question,
            "database_context": database_context,
            "answer": "",
        }
    )

    return ChatResponse(question=request.question, answer=result["answer"])
