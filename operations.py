from models import PythonCourseStudent, JavaCourseStudent
from storage import save_students


class StudentManagement:
    def __init__(self, students):
        self.students = students

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student

    def get_name(self):
        while True:
            name = input("Enter student name: ").strip().capitalize()

            if name == "":
                print("Name cannot be empty.")
                continue

            if not name.isalpha():
                print("Name must contain letters only.")
                continue

            return name

    def get_roll_number(self):
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

    def get_grade(self):
        while True:
            grade = input("Enter grade (A-F): ").strip().upper()

            if len(grade) != 1 or grade not in "ABCDEF":
                print("Grade must be one letter from A to F.")
                continue

            return grade

    def get_scholarship_percent(self):
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

    def get_course(self):
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

    def add_student(self):
        name = self.get_name()

        while True:
            roll_number = self.get_roll_number()

            if self.find_student(roll_number) is None:
                break
            else:
                print("This roll number already exists. Enter a different number.")

        grade = self.get_grade()
        scholarship = self.get_scholarship_percent()
        course = self.get_course()

        if course == "Python":
            student = PythonCourseStudent(name, roll_number, grade, scholarship)
        else:
            student = JavaCourseStudent(name, roll_number, grade, scholarship)

        self.students.append(student)
        save_students(self.students)
        print("Student added successfully.")

    def show_all_students(self):
        if len(self.students) == 0:
            print("There are no students.")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        roll_number = self.get_roll_number()
        student = self.find_student(roll_number)

        if student is not None:
            student.display()
        else:
            print("Student not found.")

    def update_grade(self):
        roll_number = self.get_roll_number()
        student = self.find_student(roll_number)

        if student is not None:
            student.grade = self.get_grade()
            save_students(self.students)
            print("Grade updated successfully.")
        else:
            print("Student not found.")