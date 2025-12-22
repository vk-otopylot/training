# Student Record System

# students = []
#
# n = int(input('Number of student you want to add: '))
#
# for i in range(n):
#     roll = int(input('Enter the roll no of the student: '))
#     name = input('Enter the name of the student: ')
#     mark = float(input('Enter the mark of the student '))
#
#     stu = {
#         'roll': roll,
#         'name': name,
#         'mark': mark,
#     }
#     students.append(stu)
#
# highest = students[0]
#
# for student in students:
#     if student['mark'] > highest['mark']:
#         highest = student
#
# print(highest)



# Group Elements by Frequency - Convert list into dictionary of element counts.

# freq = {}
#
# li = [1,4,3,5,6,1,4,15,45,15,45,35,45]
#
# for i in li:
#     # print(i)
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
#
# print(freq)

# Inventory Management
#
# product_dict = {
#     'hand_wash': 20,
#     'soap': 12,
#     'shampoo': 10,
#     'hair_oil': 34,
#     'body_lotion': 4,
# }
#
# u_inp = input('Enter the product name you want to update quantity: ')
# quan = int(input('Enter the new quantity: '))
#
# product_dict['u_ipt'] = quan
#
# print(f'Quantity updated successfully. {u_inp}: {product_dict['u_ipt']}')


# Count Character Frequency

# text = 'Hello, my name is vivek kakadia and i am from surat. and i want to make my career bright.'
#
# freq = {}
#
# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
#
# print(freq)


# Remove Student by Roll Number

students = [{'roll': 101, 'name': 'vivek', 'mark': 89.0},
{'roll': 102, 'name': 'shani', 'mark': 56.0}]

roll_no = int(input('Enter the roll_no of the student you want to remove: '))

for student in students:
    if student['roll'] == roll_no:
        students.remove(student)

print(students)