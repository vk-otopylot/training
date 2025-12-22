# Palindrome Check

# For Number

# value = int(input('Enter any Number to check whether it is palindrome or not: '))
# og = value
# res = 0
# while value > 0:
#     last = value % 10
#     res = (res * 10) + last
#     value = value // 10
#
# if og == res:
#     print('Palindrome')
# else:
#     print('Not Palindrome')


# For String

# text = input('Enter any string to check whether is is palindrome or not: ')
#
# res = text[::-1]
#
# if res == text:
#     print('Palindrome')
# else:
#     print('Not Palindrome')


# Armstrong Number

# total = 0
# num = int(input('Enter the Number to check whether it is armstrong or not: '))
# og = num
# str_num = str(num)
# size = len(str_num)
#
# while num > 0:
#     last = num % 10
#     total = total + (last ** size)
#     num = num // 10
#
# if total == og:
#     print('Armstrong')
# else:
#     print('Not Armstrong')


# Number Guessing Game

# num = 25
#
# while True:
#     u_inp = int(input('Enter the Number: '))
#     if u_inp > num:
#         print('Lower Please')
#     elif u_inp < num:
#         print('Higher Please ')
#     elif u_inp == num:
#         print('Correct Guess.!!!')
#         break
#     else:
#         print('Invalid choice.')


# Find Missing Number in list

# num_li = []
#
# num = int(input('Enter the Number till you want to generate list: '))
#
# for i in range(1,num+1):
#     if i == 9:
#         continue
#     num_li.append(i)
#
# expected_sum = num * (num+1) // 2
# actual_sum = sum(num_li)
#
# m = expected_sum - actual_sum
# print(m)


# Simple Voting System
#
# vote_count = {
#         'BJP': 0,
#         'Congress': 0,
#         'AAP': 0,
#         'NOTA': 0
#     }
#
# while True:
#     choice = input('Please Choose any one from below Option\n1. BJP\n2. Congress\n3. AAP\n4. NOTA\n5. Exit\n')
#     if choice == '1':
#         vote_count['BJP'] += 1
#     elif choice == '2':
#         vote_count['Congress'] += 1
#     elif choice == '3':
#         vote_count['AAP'] += 1
#     elif choice == '4':
#         vote_count['NOTA'] += 1
#     elif choice == '5':
#         break
#     else:
#         print('Invalid Choice.')
#
# for key,value in vote_count.items():
#     print(f'{key}: {value}')


# Expense Tracker - Calculate Total Expense

expense = {
    'education': 12000,
    'personal': 2500,
    'electricity': 1800,
    'petrol': 800,
    'food': 1500,
}

total_expense = 0

for value in expense.values():
    total_expense = total_expense + value

print(total_expense)