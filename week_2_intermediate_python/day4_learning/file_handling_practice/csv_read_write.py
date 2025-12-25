import csv
import json

# Export Employee Salary Data to CSV

# employees = [
#     [101,'vivek',12500],
#     [102,'shani',11400],
#     [103,'hardeep',14000]
# ]
# header = ['id','name','salary']
#
# with open('employees.csv', 'w', newline='') as file:
#     csvwriter = csv.writer(file)
#     csvwriter.writerow(header)
#     csvwriter.writerows(employees)


# Read Employee Salary CSV & Calculate Net Salary - Add 5% Bonus

# with open('employees.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     next(csvreader)
#     for data in csvreader:
#         e_id, name, salary = data
#         sal = int(salary)
#         net_salary = sal + (sal * 5) / 100
#         print(e_id,name,net_salary)


# Convert CSV → JSON

# data = []
#
# with open('products.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     next(csvreader)
#     for item in csvreader:
#         dict1 = {
#             'id': item[0],
#             'name': item[1],
#             'price': item[2]
#         }
#         data.append(dict1)
#
# with open('products.json', 'w') as file:
#     json.dump(data,file,indent=4)

with open('products.csv', 'r') as file:
    csvreader = csv.DictReader(file)
    for data in csvreader:
        print(dict(data))


