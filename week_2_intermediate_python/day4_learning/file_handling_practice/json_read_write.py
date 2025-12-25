# Save Student Records to JSON File

import json
import csv
from json import JSONDecodeError

# students = [
#     {"roll":1,"name":"vivek","marks":85},
#     {"roll":2,"name":"shani","marks":58},
#     {"roll":3,"name":"hardeep","marks":67}
# ]
#
# with open('students.json', 'w') as file:
#     json.dump(students, file, indent=4)

# Load Student Records from JSON File

# try:
#     with open('students.json', 'r') as file:
#         data = json.load(file)
#
#     for item in data:
#         if item['marks'] > 80:
#             print(item)
#
# except FileNotFoundError as e:
#     print(e)
#
# except JSONDecodeError as j:
#     print(j)


# Append New Student to Existing JSON File

# n_data = {"roll": 4, "name": 'ayush', "marks": 47}
#
# students = []
# try:
#     with open('students.json', 'r') as file:
#         students = json.load(file)
#
# except FileNotFoundError as f:
#     print(f)
# except PermissionError as p:
#     print(p)
# except JSONDecodeError as j:
#     print(j)
#
# students.append(n_data)
#
# try:
#     with open('students.json', 'w') as file:
#         json.dump(students, file, indent=4)
#
# except PermissionError as p:
#     print(p)


# Convert JSON → CSV

data = []
try:
    with open('orders.json', 'r') as file:
        data = json.load(file)
except Exception as e:
    print(e)

fields = ['name','Mobile_no','address','amount']

with open('orders.csv', 'w', newline='') as file:
    csvwriter = csv.DictWriter(file, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(data)
