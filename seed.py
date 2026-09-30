from app.core.database import SessionLocal, init_db
from app.models.student import Student

SAMPLE_STUDENTS = [
    {
        "name": "Aarav Sharma",
        "email": "aarav@example.com",
        "age": 20,
        "course": "BCA",
        "semester": 4,
        "cgpa": 8.4,
    },
    {
        "name": "Priya Das",
        "email": "priya@example.com",
        "age": 21,
        "course": "BCA",
        "semester": 4,
        "cgpa": 9.1,
    },
    {
        "name": "Rahul Sen",
        "email": "rahul@example.com",
        "age": 20,
        "course": "BCA",
        "semester": 3,
        "cgpa": 7.8,
    },
    {
        "name": "Ananya Roy",
        "email": "ananya@example.com",
        "age": 19,
        "course": "BCA",
        "semester": 2,
        "cgpa": 8.7,
    },
]


init_db()
db = SessionLocal()

try:
    if db.query(Student).count() == 0:
        db.add_all([Student(**student) for student in SAMPLE_STUDENTS])
        db.commit()
        print("Sample students added successfully.")
    else:
        print("Database already contains students. No sample data added.")
finally:
    db.close()
