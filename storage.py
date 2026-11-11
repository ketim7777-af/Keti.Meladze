import json
from models import PythonCourseStudent, JavaCourseStudent


initial_students = [
    PythonCourseStudent("Keti", 1, "A", 0),
    JavaCourseStudent("Irakli", 2, "B", 25),
    PythonCourseStudent("Lela", 3, "C", 50),
    JavaCourseStudent("Niko", 4, "D", 100)
]


def load_students():
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            students_data = json.load(file)

    except FileNotFoundError:
        return initial_students.copy()

    except json.JSONDecodeError:
        print("JSON file has an incorrect format.")
        return initial_students.copy()

    students_list = []

    for student_data in students_data:
        name = student_data["name"]
        roll_number = student_data["roll_number"]
        grade = student_data["grade"]
        scholarship_percent = student_data["scholarship_percent"]
        course = student_data["course"]

        if course == "Python":
            student = PythonCourseStudent(name, roll_number, grade, scholarship_percent)
        else:
            student = JavaCourseStudent(name, roll_number, grade, scholarship_percent)

        students_list.append(student)

    return students_list


def save_students(students):
    students_data = []

    for student in students:
        student_data = {
            "name": student.name,
            "roll_number": student.roll_number,
            "grade": student.grade,
            "scholarship_percent": student.scholarship_percent,
            "course": student.get_course_name()
        }
        students_data.append(student_data)

    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students_data, file, indent=4, ensure_ascii=False)