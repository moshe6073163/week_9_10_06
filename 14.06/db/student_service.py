from db import student_repository

def create_student(name: str, age: int, course: str, email: str | None, status: str = "active"):
    if len(name) < 2:
        return False
    return student_repository.create_student(name,age,course,email,status)