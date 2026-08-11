from student import Student
from storage import load_students, save_students


def add_student(students):
    try:
        roll_no = int(input("Enter roll number: "))
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        course = input("Enter course: ").strip()
        marks = float(input("Enter marks: "))

        for s in students:
            if s.roll_no == roll_no:
                print("A student with this roll number already exists.")
                return

        students.append(Student(roll_no, name, age, course, marks))
        save_students(students)
        print("Student added successfully.")

    except ValueError:
        print("Invalid input. Roll number/age must be numbers, marks must be a number.")


def view_students(students):
    if not students:
        print("No student records found.")
        return
    for s in students:
        s.display()


def search_student(students):
    try:
        roll_no = int(input("Enter roll number to search: "))
        for s in students:
            if s.roll_no == roll_no:
                s.display()
                return
        print("Student not found.")
    except ValueError:
        print("Invalid roll number.")

def filter_students(students):
    print("Filter by: 1. Course   2. Minimum Marks")
    option = input("Enter choice (1 or 2): ").strip()

    if option == "1":
        course = input("Enter course to filter by: ").strip().lower()
        results = [s for s in students if s.course.lower() == course]
    elif option == "2":
        try:
            min_marks = float(input("Enter minimum marks: "))
            results = [s for s in students if s.marks >= min_marks]
        except ValueError:
            print("Invalid marks value.")
            return
    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching students found.")
    else:
        for s in results:
            s.display()


def update_student(students):
    try:
        roll_no = int(input("Enter roll number to update: "))
        for s in students:
            if s.roll_no == roll_no:
                s.name = input(f"New name (was {s.name}): ").strip() or s.name
                s.age = int(input(f"New age (was {s.age}): ") or s.age)
                s.course = input(f"New course (was {s.course}): ").strip() or s.course
                s.marks = float(input(f"New marks (was {s.marks}): ") or s.marks)
                save_students(students)
                print("Student updated successfully.")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input.")


def delete_student(students):
    try:
        roll_no = int(input("Enter roll number to delete: "))
        for s in students:
            if s.roll_no == roll_no:
                students.remove(s)
                save_students(students)
                print("Student deleted successfully.")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid roll number.")


def main():
    students = load_students()

    menu = """
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Filter Students
7. Exit
======================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)        
        elif choice == "6":
            filter_students(students)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-7.")


if __name__ == "__main__":
    main()