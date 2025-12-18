# Add Student Record (Append)

# import csv
#
# roll_no = input('Enter roll number of the student: ')
# name = input('Enter name of the student: ')
# mark = input('Enter mark of the student: ')
#
# value = [roll_no, name, mark]
#
# with open('students.csv', mode= 'a', newline='') as file:
#     csvwriter = csv.writer(file)
#     csvwriter.writerow([roll_no, name, mark])


# View All Students (Read)

# import csv
#
# with open('students.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         for col in row:
#             print(col, end=" ")
#         print()


# Search Student by Roll No

# import csv
#
# roll_no = input('Enter student roll no: ')
#
# with open('students.csv' , 'r') as file:
#     csvreader = csv.reader(file)
#     for data in csvreader:
#         if data[0] == roll_no:
#             print(data[0])
#             print(data[1])
#             print(data[2])
#             break
#         else:
#             print('Student details not found ')

# Update Student Marks

# import csv
#
# roll_no = input('Enter student roll no: ')
# new_marks = input('Enter new mark: ')
#
# rows = []
# found = False
#
# with open('students.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     for data in csvreader:
#         rows.append(data)
#
# for row in rows:
#     if row[0] == roll_no:
#         row[2] = new_marks
#         found = True
#         break
#
# if found:
#     with open('students.csv', 'w', newline='') as file:
#         csvwriter = csv.writer(file)
#         csvwriter.writerows(rows)

# Delete Student Record

import csv

rows = []
found = False

roll_no = input('Enter students roll number that you want to delete: ')

with open ('students.csv', 'r') as file:
    csvreader = csv.reader(file)
    for data in csvreader:
        if data[0] != roll_no:
            rows.append(data)

with open('students.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(rows)