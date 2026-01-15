import json

# Create a JSON file from a Python dictionary.

# student = {
#     'name': 'vivek',
#     'roll_no': 101,
#     'age': 21,
#     'class': 12,
#     'grade': 'A'
# }
#
# data = json.dumps(student, indent=4)
#
# with open('student.json', 'w') as f:
#     f.write(data)


# Write a list of dictionaries into a JSON file.

data = [{"name": "vivek", "age": 21, "marks": 89}, {"name": "shani", "age": 21, "marks": 56}, {"name": "hardeep", "age": 21, "marks": 78}, {"name": "jaymin", "age": 21, "marks": 76}, {"name": "ayush", "age": 21, "marks": 53}]

result = json.dumps(data, indent=4)
with open('students.json', 'w') as f:
    f.write(result)