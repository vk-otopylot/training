print('Welcome to the ATM. ')
print('Enter your choice:')

total_balance = 2300

choice = input('1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n')

if choice == '1':
    print(f'your available balance is: {total_balance}')

elif choice == '2':
    deposit_money = float(input('Enter amount to Deposit: '))
    total_balance = total_balance + deposit_money
    print(f'your available balance is: {total_balance}')

elif choice == '3':
    withdraw_money = float(input('Enter amount to Withdraw: '))
    if withdraw_money > total_balance:
        print('you do not have enough money to withdraw.')
    else:
        total_balance = total_balance - withdraw_money
        print(f'your available balance is: {total_balance}')

else:
    print('Invalid Choice')