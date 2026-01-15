import json

# Parse a JSON string and print all keys.
#
# json_string = '{"name": "vivek", "age": 21, "address": "surat"}'
#
# data = json.loads(json_string)
# for key in data.keys():
#     print(key)


# Read a JSON file and display all student names.

# with open('s_details.json', 'r') as file:
#     data = json.load(file)
#
# for val in data.values():
#     for i in val:
#         print(i['name'])


# Convert JSON data into Python dictionary and list.

with open('s_details.json', 'r') as file:
    data = json.load(file)

print(type(data))
print(type(data['students']))
