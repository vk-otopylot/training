year = int(input("Enter Year to know year is leap year or not: "))

if year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')