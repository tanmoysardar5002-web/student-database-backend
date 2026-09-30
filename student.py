from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=15, le=100)
    course: str = Field(..., min_length=2, max_length=100)
    semester: int = Field(..., ge=1, le=12)
    cgpa: float = Field(..., ge=0, le=10)


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    email: EmailStr | None = None
    age: int | None = Field(None, ge=15, le=100)
    course: str | None = Field(None, min_length=2, max_length=100)
    semester: int | None = Field(None, ge=1, le=12)
    cgpa: float | None = Field(None, ge=0, le=10)


class StudentResponse(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
