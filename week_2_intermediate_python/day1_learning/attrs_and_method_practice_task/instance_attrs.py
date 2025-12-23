# Create Student Records with Individual Marks

# class Student:
#     def __init__(self, name, roll_no, mark):
#         self.name = name
#         self.roll_no = roll_no
#         self.mark = mark
#         print(f'name={self.name}, roll_no={self.roll_no}, mark={self.mark}')
#
# s1 = Student('vivek', 101, 89)
# s2 = Student('shani', 102, 56)
# s3 = Student('hardeep', 103, 78)


# Create Bank Accounts with Different Balances

class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

        print(f'Account_no: {self.account_no}')
        print(f'Holder_name: {self.holder_name}')
        print(f'balance: {self.balance}')

b1 = BankAccount(12345678, 'vivek_kakadia', 23500)
b2 = BankAccount(87654321, 'shani_k', 21000)