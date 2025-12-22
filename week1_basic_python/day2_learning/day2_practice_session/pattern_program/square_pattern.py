# column = int(input('Enter the column number: '))
# rows = int(input('Enter the row number: '))

#Using nested Loop

# for i in range(1,column+1):
#     for j in range(1,rows+1):
#         print("*", end='')
#     print()

#Using range() function

no = int(input('Enter the number you want to see square pattern: '))

for i in range(1, no+1):
    print('*' * no)