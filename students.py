from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.student import StudentCreate, StudentResponse, StudentUpdate
from app.services import student_service

router = APIRouter()


@router.post("/", response_model=StudentResponse, status_code=201, summary="Create a student")
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student(db, data)


@router.get("/", response_model=list[StudentResponse], summary="Get all students")
def get_students(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return student_service.get_students(db, skip, limit)


@router.get("/search", response_model=list[StudentResponse], summary="Search students")
def search_students(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    return student_service.search_students(db, q)


@router.get("/{student_id}", response_model=StudentResponse, summary="Get a student")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_student(db, student_id)


@router.put("/{student_id}", response_model=StudentResponse, summary="Update a student")
def update_student(student_id: int, data: StudentUpdate, db: Session = Depends(get_db)):
    return student_service.update_student(db, student_id, data)


@router.delete("/{student_id}", summary="Delete a student")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.delete_student(db, student_id)
