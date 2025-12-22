from datetime import datetime

# Current Date & Time

# print(datetime.datetime.now())


# Extract Date Parts

# now = datetime.now().date()
#
# print(now.year)
# print(now.month)
# print(now.day)


# Days Difference
#
# today = datetime.now().date()
# user_date = input("Enter a date (YYYY-MM-DD): ")
#
# given_date = datetime.strptime(user_date, "%Y-%m-%d").date()
#
# diff = today - given_date
#
# print(diff.days)


# Format Date

today = datetime.now().date()

print(today.strftime('%d-%m-%Y'))
