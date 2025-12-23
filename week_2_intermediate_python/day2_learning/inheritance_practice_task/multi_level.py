# Person → Employee → Manager Hierarchy

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Employee(Person):
#     def __init__(self,e_id, salary, name, age):
#         super().__init__(name, age)
#         self.e_id = e_id
#         self.salary = salary
#
# class Manager(Employee):
#     def __init__(self, department, e_id, salary, name, age):
#         super().__init__(e_id, salary, name, age)
#         self.department = department
#
#     def display_emp_details(self):
#         print(f'Employee_id: {self.e_id}, Department: {self.department}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}')
#
# p1 = Person('vivek k', 21)
# emp1 = Employee(101, 12500, 'vivek k', 21)
# man1 = Manager('IT',101, 12500, 'vivek k', 21)
# man1.display_emp_details()

# Vehicle → Car → ElectricCar System

class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

class Car(Vehicle):
    def __init__(self, brand, v_type):
        super().__init__(v_type)
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, b_capacity, brand, v_type):
        super().__init__(brand, v_type)
        self.b_capacity = b_capacity

    def vehicle_details(self):
        print(f'Vehicle_Type : {self.v_type}, Brand: {self.brand}, Battery_capacity: {self.b_capacity}')

car1 = ElectricCar('80kWh', 'skoda', 'EV')
car1.vehicle_details()