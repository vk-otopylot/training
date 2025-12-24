# Counter Practice Programs

from collections import Counter

# Character Frequency Counter in a String

# text = 'Hello my name is vivek kakadia. i am from surat and i want to make my career bright.'
#
# counter = Counter(text)
# print(counter)

# Word Frequency Analyzer

# text = 'Hello my name is vivek kakadia. i am from surat and i want to make my career bright.'
# n_text = text.split()
# res = Counter(n_text)
#
# print(res.values())


# defaultdict Practice Programs

# Group Students by Course

# from collections import defaultdict
#
# students = [ ('vivek', 'BCA'), ('hardeep', 'BCA'), ('meet', 'MCA'), ('dhruvil', 'Bsc IT'), ('tushal', 'BA')]
#
# dict1 = defaultdict(list)
# for k, v in students:
#     dict1[v].append(k)
#
# for key, val in dict1.items():
#     print(key, val)


# Word Length Grouping

# from collections import defaultdict
#
# words = ["apple", "cat", "dog", "banana", "ball", "ant", "mango"]
#
# dict1 = defaultdict(list)
#
# for word in words:
#     dict1[len(word)].append(word)
#
# print(dict1)

# Employee Department Grouping

# from collections import defaultdict
# employees = [('vivek', 'IT'), ('hardeep', 'finance'), ('jaymeen', 'construction'), ('piyush', 'construction'), ('meet', 'IT'), ('om', 'data_handling')]
#
# dict1 = defaultdict(list)
#
# for k,v in employees:
#     dict1[v].append(k)
#
# for key,val in dict1.items():
#     print(f'{key}-> {val}')


# namedtuple Practice Programs

# from collections import namedtuple
#
# Student = namedtuple('Student', ['roll_no','name','marks'])
#
# s1 = Student(101,'vivek',89)
# s2 = Student(102,'shani',56)
#
# print(s1)
# print(s2)


# Combined Practice

# Attendance Tracking System

from collections import Counter, namedtuple, defaultdict

Student = namedtuple('Student', ['roll_no', 'name'])

students = [
    Student(1, 'vivek'),
    Student(2, 'hardeep'),
    Student(3, 'shani'),
    Student(4, 'meet'),
    Student(5, 'om'),
    Student(6, 'ayush')
]

attendance = [
    (1, "Present"), (2, "Present"), (3, "Absent"),  (4, "Present"),
    (1, "Present"), (2, "Absent"),  (3, "Present"), (4, "Present"),
    (1, "Absent"),  (2, "Present"), (3, "Present"), (4, "Absent"),
]

attendance_sheet = defaultdict(list)

for roll, status in attendance:
    attendance_sheet[roll].append(status)

# print(attendance_sheet)

present_count = {}

for roll, records in attendance_sheet.items():
    present_count[roll] = Counter(records)["Present"]

print(present_count)