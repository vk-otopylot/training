# li = []
#
# for i in range(1,6):
#     name = input('Enter the name of the Student: ')
#     age =  input('Enter the age of the Student: ')
#     li.append([name,age])

# print(li)

# for i in li:
#     print(i)


#Print only name

# students = [
#     ["Amit", 20],
#     ["Vivek", 22],
#     ["Rahul", 19]
# ]

# for student in students:
#     print(student[0])



# Max mark from nested list

# marks = [
#     ["Amit", 78],
#     ["Vivek", 90],
#     ["Neha", 85],
# ]

# sorted_marks = []
#
# for i in marks:
#     sorted_marks.append(i[1])
#
# result = sorted(sorted_marks, reverse=True)
# print(result[0])


# Insert student at specific position

# marks = [
#     ["Amit", 78],
#     ["Vivek", 90],
#     ["Neha", 85],
# ]
#
# name = input('Enter the name of the student: ')
# mark = int(input('Enter the mark of the student: '))
#
# marks.insert(2, [name,mark])
#
# print(marks)


# Remove a sub-list

# students = [
#     ["Amit", 78],
#     ["Vivek", 90],
#     ["Hardip", 85],
#     ["shani", 67],
#     ["Bhargava", 71],
# ]
#
# rm_student = input('Enter the name of the student you want to remove: ')
#
# for student in students:
#     if student[0] == rm_student:
#         students.remove(student)
#         break

# print(students)


# Sort nested list by names
#
# students = [
#     ["Amit", 78],
#     ["Vivek", 90],
#     ["Hardip", 85],
#     ["shani", 67],
#     ["Bhargava", 71],
# ]
#
# students.sort(key= lambda x: x[0])
#
# print(students)


# Sort nested list by marks
#
# students = [
#     ["Amit", 78],
#     ["Vivek", 90],
#     ["Hardip", 85],
#     ["shani", 67],
#     ["Bhargava", 71],
# ]
#
# students.sort(key= lambda x: x[1], reverse=True)
#
# print(students)


# Create 3x3 matrix

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        val = int(input('Enter the value: '))
        row.append(val)
    matrix.append(row)

# Sum of each row

for k in range(3):
    row_sum = 0
    for l in range(3):
        row_sum = row_sum + matrix[k][l]
    print(row_sum)