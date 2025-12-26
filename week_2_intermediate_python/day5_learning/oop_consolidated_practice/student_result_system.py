from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @abstractmethod
    def calculate_result(self):
        pass

    def calculate_percentage(self):
        total_obtained = sum(self.marks.values())
        total_subjects = len(self.marks)
        return total_obtained / total_subjects

class SchoolStudent(Student):
    def calculate_result(self):
        percentage = self.calculate_percentage()

        status = "Pass" if percentage >= 33 else "Fail"

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        print("\n--- School Student Result ---")
        print(f"Name       : {self.name}")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Status     : {status}")
        print(f"Grade      : {grade}")


class CollegeStudent(Student):
    def calculate_result(self):
        percentage = self.calculate_percentage()

        status = "Pass" if percentage >= 40 else "Fail"

        if percentage >= 85:
            grade = "Distinction"
        elif percentage >= 70:
            grade = "First Class"
        elif percentage >= 55:
            grade = "Second Class"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("\n--- College Student Result ---")
        print(f"Name       : {self.name}")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Status     : {status}")
        print(f"Grade      : {grade}")

# stu1 = SchoolStudent('vivek',{'math':56,'history':90,'science':67})
# stu1.calculate_result()

stu1 = CollegeStudent('vivek',{'math':56,'history':90,'science':67})
stu1.calculate_result()