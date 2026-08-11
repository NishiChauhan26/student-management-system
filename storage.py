import json
import os
from student import Student

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return [Student.from_dict(item) for item in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    data = [s.to_dict() for s in students]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)