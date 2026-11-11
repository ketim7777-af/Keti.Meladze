from models import PythonCourseStudent, JavaCourseStudent
from storage import save_students


def find_student(students, roll_number):
    for student in students:
        if student.roll_number == roll_number:
            return student    


def get_name():
    while True:
        name = input("Enter student name: ").strip().capitalize()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.isalpha():
            print("Name must contain letters only.")
            continue

        return name


def get_roll_number():
    while True:
        roll_number = input("Enter roll number: ").strip()

        if roll_number == "":
            print("Roll number cannot be empty.")
            continue

        try:
            roll_number = int(roll_number)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if roll_number <= 0:
            print("Roll number must be greater than 0.")
            continue

        return roll_number


def get_grade():
    while True:
        grade = input("Enter grade (A-F): ").strip().upper()

        if len(grade) != 1 or grade not in "ABCDEF":
            print("Grade must be one letter from A to F.")
            continue

        return grade


def get_scholarship_percent():
    while True:
        try:
            scholarship = int(input("Enter scholarship percentage: ").strip())
        except ValueError:
            print("Please enter a number.")
            continue

        if not 0 <= scholarship <= 100:
            print("Scholarship must be between 0 and 100.")
            continue

        return scholarship


def get_course():
    while True:
        print("Choose a course:")
        print("1. Python")
        print("2. Java")

        choice = input("Choose an option: ").strip()

        if choice not in ("1", "2"):
            print("Please choose 1 or 2.")
            continue

        if choice == "1":
            return "Python"

        else:
            return "Java"


def add_student(students):
    name = get_name()

    while True:
        roll_number = get_roll_number()

        if find_student(students, roll_number) is None:
            break
        else:
            print("This roll number already exists. Enter a different number.")

    grade = get_grade()
    scholarship = get_scholarship_percent()
    course = get_course()

    if course == "Python":
        student = PythonCourseStudent(name, roll_number, grade, scholarship)
    else:
        student = JavaCourseStudent(name, roll_number,grade, scholarship)

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def show_all_students(students):
    if len(students) == 0:
        print("There are no students.")
        return

    for student in students:
        student.show_info()


def search_student(students):
    roll_number = get_roll_number()
    student = find_student(students, roll_number)

    if student is not None:
        student.show_info() # ეს შოუ ინფო სხვაგან სად წერია? საიდან მოვიდა?
    else:
        print("Student not found.")


def update_grade(students):
    roll_number = get_roll_number()
    student = find_student(students, roll_number)

    if student is not None:
        student.grade = get_grade()
        save_students(students)
        print("Grade updated successfully.")
    else:
        print("Student not found.")