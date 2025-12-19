import os

import calendar
from datetime import datetime, date

def get_weekend_days(year, month):
    saturday = []
    sunday = []

    num_days = calendar.monthrange(year, month)[1]

    for i in range(1, num_days +1):
        curr_date = date(year, month, i)
        if curr_date.weekday() == 5:
            saturday.append(curr_date.strftime('%A, %B %d, %Y'))
        elif curr_date.weekday() == 6:
            sunday.append(curr_date.strftime('%A, %B %d, %Y'))
    n_list = saturday + sunday
    return n_list

# os.makedirs('2026_holidays')

os.chdir('2026_holidays')

list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in range(12):
    with open(f'{list_of_months[i]}-2026.txt', 'w') as file:
        pass

for j in range(12):
    # os.chdir(f'{list_of_months[j]}-2026.txt')
    with open(f'{list_of_months[j]}-2026.txt', 'w') as file:
        data = get_weekend_days(2026, j+1)
        for val in data:
            file.write(val + '\n')