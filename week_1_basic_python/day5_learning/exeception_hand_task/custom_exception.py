# Custom Exception – Age Validation

# class InvalidAgeError(Exception):
#     pass
#     # def __init__(self, age, message = 'Age should be between 18 to 56'):
#     #     self.age = age
#     #     self.message = message
#     #     super().__init__(self.message)
#     #
#     # def __str__(self):
#     #     return f"{self.age}: {self.message}"
#
# try:
#     age = int(input('Enter your age: '))
#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above")
#     print('Access Granted.')
#
# except InvalidAgeError as i:
#     print(i)


# Password Validation System

# class WeakPasswordError(Exception):
#     pass
#
# try:
#     password = input('Enter the password: ')
#     if len(password) < 8:
#         raise WeakPasswordError('Password should be at least 8 character.')
#     if not any(char.isdigit() for char in password) :
#         raise WeakPasswordError('password should contain digit.')
# except WeakPasswordError as w:
#     print(w)


# Banking System

class InsufficientBalanceError(Exception):
    pass

balance = 2500

try:
    deposit = input('Enter amount you want to deposit: ')
    d_amt = float(deposit)
    balance = balance + d_amt
    print('Amount deposited SuccessFully')

    withdraw = input('Enter amount you want to withdraw: ')
    w_amt = float(withdraw)
    if w_amt > balance:
        raise InsufficientBalanceError('Withdraw amount is grater than available balance.')
    elif w_amt < 0:
        raise ValueError('Withdraw amount negative.')
    else:
        balance = balance - w_amt
        print('Successfully Withdraw.')

except ValueError as v:
    print(v)

except InsufficientBalanceError as i:
    print(i)

finally:
    print(f'Your available balance is {balance}')
