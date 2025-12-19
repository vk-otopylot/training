# Divide Two Numbers Safely

# a = 5
# b = 'v'
#
# try:
#     print(a / b)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as v:
#     print(v)
# finally:
#     print('Program finished ')


# List Index Access
#
# li = [12,45,85,23,56]
#
# index = int(input('Enter the index you want to check what number placed at that index: '))
#
# try:
#     print(li[index])
# except IndexError as i:
#     print(i)
# except ValueError as v:
#     print(v)


# File Reading Program

# file = None
#
# try:
#     file = open('data.txt', 'r')
#     data = file.read()
#     print(data)
# except FileNotFoundError as f:
#     print(f)
# except PermissionError as p:
#     print(p)
# finally:
#     file.close()


# Convert String to Integer

# user_input = input('Enter any Number: ')
#
# try:
#     to_int = int(user_input)
#     print(to_int)
# except ValueError as v:
#     print(v)


# Dictionary Key Search

marks = {
    'vivek': 89,
    'shani': 67,
    'hardeep': 78,
    'kuldeep': 82,
}

name = input('Enter the name of the student, you want to get the mark: ')

try:
    print(marks[name])
except KeyError as k:
    print(f'Error:{k}')