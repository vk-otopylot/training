import csv

class NegativeSalaryError(Exception):
    def __init__(self, salary):
        super().__init__(f"Invalid Salary! Salary cannot be negative → {salary}")

def process_employee_salaries(csv_file, report_file):
    file = None
    try:
        file = open(csv_file, 'r')
        reader = csv.reader(file)
        next(reader)
        with open(report_file, 'w') as file:
            for row in reader:
                emp_id, name, salary = row
                salary = float(salary)
                if salary < 0:
                    raise NegativeSalaryError(salary)
                gross = salary + (salary * 0.15)
                deductions = salary * 0.10
                net = gross - deductions
                file.write(
                    f"Employee ID : {emp_id}\n"
                    f"Name        : {name}\n"
                    f"Base Salary : {salary}\n"
                    f"Gross Salary: {gross}\n"
                    f"Deductions  : {deductions}\n"
                    f"Net Salary  : {net}\n"
                    "---------------------------------\n"
                )

    except FileNotFoundError:
        print("Error: employees.csv file not found")
    except ValueError:
        print("Error: Invalid salary value in file")
    except NegativeSalaryError as n:
        print(n)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        if file:
            file.close()

process_employee_salaries('employees.csv', 'salary_report.txt')