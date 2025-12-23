from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self,emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_payroll(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, basic_sal, hra, da, emp_id, name):
        super().__init__(emp_id, name)
        self.basic_sal = basic_sal
        self.hra = hra
        self.da = da
        self.__tax = None

    def set_tax(self, tax):
        self.__tax = tax

    def calculate_salary(self):
        total_salary = (self.basic_sal + self.hra + self.da)
        net_salary = total_salary - ((total_salary * self.__tax) / 100)
        return net_salary

    def get_salary(self):
        salary = self.calculate_salary()
        print(f'Salary: {salary}')

    def display_payroll(self):
        net_sal = self.calculate_salary()
        print(f'Employee_id: {self.emp_id}')
        print(f'Name: {self.name}')
        print(f'Net salary: {net_sal}')

class PartTimeEmployee(Employee):
    def __init__(self, hour_worked, rph, emp_id, name):
        super().__init__(emp_id, name)
        self.hour_worked = hour_worked
        self.rph = rph

    def calculate_salary(self):
        salary = self.hour_worked * self.rph
        return salary

    def get_salary(self):
        salary = self.calculate_salary()
        print(f'Salary: {salary}')

    def display_payroll(self):
        salary = self.calculate_salary()
        print(f'Employee_id: {self.emp_id}')
        print(f'Name: {self.name}')
        print(f'salary: {salary}')

# fte1 = FullTimeEmployee(12000,3400,0,101,'vivek')
# fte1.set_tax(8)
# fte1.display_payroll()

pte1 = PartTimeEmployee(27,1250,101,'vivek')
pte1.get_salary()
pte1.display_payroll()