column = int(input('Enter the column number: '))
rows = int(input('Enter the row number: '))

for i in range(1,column+1):
    for j in range(1,rows+1):
        print("*", end='')
    print()