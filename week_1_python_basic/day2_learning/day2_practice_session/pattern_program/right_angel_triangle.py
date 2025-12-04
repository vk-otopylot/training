num = int(input('Enter the number you want to see right angel star pattern: '))

#Using nested Loop

# for i in range(1, num+1):
#     for j in range(i):
#         print('*', end='')
#     print()

#Using range() function

for i in range(1,num+1):
    print('*' * i)