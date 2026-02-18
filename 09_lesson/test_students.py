import pytest
from database import engine, SessionLocal
from models import Base, Student


Base.metadata.create_all(bind=engine)


def test_add_student():
    session = SessionLocal()

    new_student = Student(name="Test Student", age=20)
    session.add(new_student)
    session.commit()

    student = session.query(Student).filter_by(name="Test Student").first()
    assert student is not None
    assert student.age == 20

    session.delete(student)
    session.commit()
    session.close()


def test_update_student():
    session = SessionLocal()

    student = Student(name="Update Student", age=18)
    session.add(student)
    session.commit()

    student.age = 25
    session.commit()

    updated_student = session.query(Student).filter_by(name="Update Student").first()
    assert updated_student.age == 25

    session.delete(updated_student)
    session.commit()
    session.close()


def test_delete_student():
    session = SessionLocal()

    student = Student(name="Delete Student", age=22)
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted_student = session.query(Student).filter_by(name="Delete Student").first()
    assert deleted_student is None

    session.close()