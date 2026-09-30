from sqlalchemy import Column, Float, Integer, String

from app.core.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    course = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    cgpa = Column(Float, nullable=False)
