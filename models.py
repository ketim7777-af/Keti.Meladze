class Students:
    university_name = "IT Step"

    def __init__(self, name, roll_number, grade, scholarship_percent):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        self.scholarship_percent = scholarship_percent

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if isinstance(value, str):
            value = value.strip().upper()

        if isinstance(value, str) and len(value) == 1 and value in "ABCDEF":
            self._grade = value
        else:
            raise ValueError("Grade must be one letter from A to F.")

    def display(self):
        print(f"University: {Students.university_name}")
        print(f"Course: {self.get_course_name()}")
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_number}")
        print(f"Grade: {self.grade}")
        print(f"Scholarship: {self.scholarship_percent}%")
        print("=" * 20)


class PythonCourseStudent(Students):
    def __init__(self, name, roll_number, grade, scholarship_percent):
        super().__init__(name, roll_number, grade, scholarship_percent)
        self.course = "Python"

    def get_course_name(self):
        return self.course


class JavaCourseStudent(Students):
    def __init__(self, name, roll_number, grade, scholarship_percent):
        super().__init__(name, roll_number, grade, scholarship_percent)
        self.course = "Java"

    def get_course_name(self):
        return self.course