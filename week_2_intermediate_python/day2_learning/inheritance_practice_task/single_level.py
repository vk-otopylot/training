# Person to Student Information System
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Name: {self.name}, Age: {self.age}')
#
#
# class Student(Person):
#     def __init__(self, roll_no, name, age):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#
#     def display_student_info(self):
#         print(f'Name: {self.name}, Roll_no: {self.roll_no}, Age: {self.age}')
#
# p1 = Person('vivek', 21)
# p1.display_person_info()
#
# stu1 = Student(101, 'vivek k', 21)
# stu1.display_student_info()


# Basic Bank Account to Savings Account

class BankAcc:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def display_account(self):
        print(f'Acc Holder Name: {self.acc_holder}, Balance: {self.balance}')

class SavingAcc(BankAcc):
    def __init__(self, interest_rate, acc_holder, balance):
        super().__init__(acc_holder,balance)
        self.interest_rate = interest_rate

    def display_savings_info(self):
        print(f'Acc Holder Name: {self.acc_holder}, Balance: {self.balance}, Interest Rate: {self.interest_rate}')

ac1 = SavingAcc('12%', 'Vivek k', 12500)
ac1.display_savings_info()