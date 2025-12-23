class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        bonus = (self.salary * 10) / 100
        print(f'Bonus: {bonus}')
        return bonus

class SeniorEmployee(Employee):
    def calculate_bonus(self):
        basic_bonus = super().calculate_bonus()
        extra_bonus = (self.salary * 5) / 100
        total_bonus = basic_bonus + extra_bonus
        print(f'Extra Bonus: {extra_bonus}')
        print(f'Total Bonus: {total_bonus}')

emp1 = SeniorEmployee(50000)
emp1.calculate_bonus()