# Multiple Exceptions in One Except
#
# num1 = input('Enter thr first number: ')
# num2 = input('Enter thr second number: ')
#
# try:
#     no1 = int(num1)
#     no2 = int(num2)
#     print(no1/no2)
# except (ZeroDivisionError, ValueError) as e:
#     print(e)

# ATM Withdrawal System

balance = 10000

withdraw_amt = int(input('Enter the amount you want to withdraw: '))

try:
    if withdraw_amt > balance:
        raise ValueError('Amount is grater than the available balance.')
    elif withdraw_amt < 0:
        raise ValueError('Amount is negative ')
    else:
        balance = balance - withdraw_amt
        print(f'available balance {balance}')
except Exception as v:
    print(v)