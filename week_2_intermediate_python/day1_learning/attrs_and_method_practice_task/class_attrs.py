# Assign a Common College Name to All Students

# class Student:
#     college_name = 'President college'
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#
#         print(f'college name: {self.college_name}, name: {self.name}, roll_no: {self.roll_no}')
#
#
# s1 = Student('vivek', 101)
# s2 = Student('shani', 102)


# Maintain a Single Company Name for All Employees

class Employee:
    company_name = 'ITC'
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

        print(f'company_name: {Employee.company_name}, emp_id: {self.emp_id}, name: {self.name}')

e1 = Employee(101, 'vivek')
e2 = Employee(102, 'shani')