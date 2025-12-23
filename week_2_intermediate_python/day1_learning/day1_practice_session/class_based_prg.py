# Student Information Management System

# class Student:
#     def __init__(self, name, roll_no, mark):
#         self.name = name
#         self.roll_no = roll_no
#         self.mark = mark
#
#     def display_details(self):
#         print(f'Name: {self.name}, Roll_no: {self.roll_no}, Mark: {self.mark}')
#
# s1 = Student('vivek', 101, 89)
# s1.display_details()

# Employee Salary Management System

class Employee:
    company_name = 'ITC'
    def __init__(self, e_id, name, monthly_salary):
        self.e_id = e_id
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        annual_sal = self.monthly_salary * 12
        print(f'Annual salary is: {annual_sal}')

emp1 = Employee(101, 'vivek k', 15000)
emp1.calculate_annual_salary()