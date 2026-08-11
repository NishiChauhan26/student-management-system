# Student Management System

A Python-based console application to manage student records efficiently, built using Object-Oriented Programming (OOP) and file handling. Developed as part of the Python Development Internship at Kinetrexa Software Private Limited.

## Features

- **Add Student** – Create a new student record with roll number, name, age, course, and marks
- **View All Students** – Display all stored student records
- **Search Student** – Find a specific student by roll number
- **Update Student** – Modify an existing student's details
- **Delete Student** – Remove a student record
- **Filter Students** – Filter records by course or by minimum marks
- **Persistent Storage** – All data is saved to `students.json` and reloaded automatically on the next run
- **Exception Handling** – Handles invalid input and missing/corrupted data files gracefully

## Project Structure
student_management_system/
├── student.py # Student class (OOP blueprint) with to_dict/from_dict for file storage
├── storage.py # Functions to save/load student data to/from students.json
├── main.py # CRUD operations and the menu-driven program entry point
├── students.json # Auto-generated data file (created on first run)
└── README.md

## Technologies Used

- Python 3
- Built-in `json` module for data persistence
- Object-Oriented Programming (classes, objects, static methods)

## How to Run

1. Clone this repository: git clone <your-repo-url>
2. Navigate into the project folder: cd student_management_system
3. Run the program: python main.py
4. Follow the on-screen menu to add, view, search, update, delete, or filter student records.

## Sample Menu
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Filter Students
7. Exit
   
======================================

## Author

Nishi Chauhan

Python Development Intern
