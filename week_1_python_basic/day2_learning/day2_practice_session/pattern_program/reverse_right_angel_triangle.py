num = int(input('Enter the number you want to show reverse right angel star pattern: '))

#Using nested Loop

# for i in range(1, num+1):
#     for j in range(num-i+1):
#         print("*", end='')
#     print()

#Using range() function

for i in range(num, 0, -1):
    print('*' * i)