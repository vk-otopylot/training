from collections import namedtuple, defaultdict

Students = namedtuple('Students', ['name', 'roll_no'])

students_records = [
    Students('vivek',101),
    Students('shani', 102),
    Students('hardeep', 103),
    Students('meet', 104),
    Students('om', 105),
]

dict1 = defaultdict(list)

class AttendanceSystem:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no  = roll_no
    def mark_present(self):
        dict1[self.roll_no].append('present')
    def mark_absent(self):
        dict1[self.roll_no].append('absent')
    def show_attendance(self):
        print(dict1[self.roll_no])
    def show_percentage(self):
        records = dict1[self.roll_no]
        present = records.count("present")
        total = len(records)
        percentage = (present / total) * 100
        print(f'Attendance Percentage = {percentage:.2f}%')

stu1 = AttendanceSystem('vivek', 101)
stu1.mark_present()
stu1.mark_absent()
stu1.mark_present()
stu1.show_attendance()
stu1.show_percentage()