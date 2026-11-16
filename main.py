from models import Students
from storage import StudentStorage
from operations import StudentManagement

class StudentManagementApp:
    def __init__(self):
        self.storage = StudentStorage()
        self.students = self.storage.load_students()
        self.student_management = StudentManagement(self.students, self.storage)

    def run(self):
        while True:
            print(f"\n{Students.university_name}")
            print("Student Management System")
            print("1. Add new student")
            print("2. View all students")
            print("3. Search student by roll number")
            print("4. Update student's grade")
            print("5. Exit")
            print("-" * 20)

            choice = input("Choose an option: ").strip()
            print("-" * 20)

            if choice == "1":
                self.student_management.add_student()
            elif choice == "2":
                self.student_management.show_all_students()
            elif choice == "3":
                self.student_management.search_student()
            elif choice == "4":
                self.student_management.update_grade()
            elif choice == "5":
                self.storage.save_students(self.students)
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    app = StudentManagementApp()
    app.run()