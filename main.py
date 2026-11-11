from models import Students
from storage import load_students, save_students
from operations import add_student, show_all_students, search_student, update_grade

def main():
    students = load_students()

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
            add_student(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_grade(students)
        elif choice == "5":
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()