import json
from pathlib import Path

from app.models import Course, Student


DATA_DIR = Path("data")
STUDENTS_FILE = DATA_DIR / "students.txt"
COURSES_FILE = DATA_DIR / "courses.txt"
REGISTRATIONS_FILE = DATA_DIR / "registrations.txt"


def save_data(students, courses, registrations):
    DATA_DIR.mkdir(exist_ok=True)

    with STUDENTS_FILE.open("w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)

    with COURSES_FILE.open("w", encoding="utf-8") as file:
        json.dump([course.to_dict() for course in courses], file, indent=4)

    with REGISTRATIONS_FILE.open("w", encoding="utf-8") as file:
        json.dump(registrations, file, indent=4)


def load_data():
    DATA_DIR.mkdir(exist_ok=True)
    return load_students(), load_courses(), load_registrations()


def load_students():
    if not STUDENTS_FILE.exists():
        return []

    try:
        with STUDENTS_FILE.open("r", encoding="utf-8") as file:
            return [Student.from_dict(item) for item in json.load(file)]
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Could not load students data. Starting with an empty student list.")
        return []


def load_courses():
    if not COURSES_FILE.exists():
        return []

    try:
        with COURSES_FILE.open("r", encoding="utf-8") as file:
            return [Course.from_dict(item) for item in json.load(file)]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Could not load courses data. Starting with an empty course list.")
        return []


def load_registrations():
    if not REGISTRATIONS_FILE.exists():
        return []

    try:
        with REGISTRATIONS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Could not load registration data. Starting with an empty list.")
        return []

    clean_registrations = []
    for item in data:
        if isinstance(item, dict) and "student_id" in item and "course_id" in item:
            clean_registrations.append(item)
    return clean_registrations
