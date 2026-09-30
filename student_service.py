from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


def create_student(db: Session, data: StudentCreate):
    student = Student(**data.model_dump())
    db.add(student)
    try:
        db.commit()
        db.refresh(student)
        return student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A student with this email already exists.")


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).order_by(Student.id).offset(skip).limit(limit).all()


def get_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student


def update_student(db: Session, student_id: int, data: StudentUpdate):
    student = get_student(db, student_id)
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(student, key, value)
    try:
        db.commit()
        db.refresh(student)
        return student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A student with this email already exists.")


def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully.", "id": student_id}


def search_students(db: Session, query: str):
    pattern = f"%{query}%"
    return (
        db.query(Student)
        .filter(
            (Student.name.ilike(pattern))
            | (Student.email.ilike(pattern))
            | (Student.course.ilike(pattern))
        )
        .order_by(Student.id)
        .all()
    )


def get_database_context(db: Session):
    students = db.query(Student).order_by(Student.id).all()
    return [
        {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "age": student.age,
            "course": student.course,
            "semester": student.semester,
            "cgpa": student.cgpa,
        }
        for student in students
    ]
