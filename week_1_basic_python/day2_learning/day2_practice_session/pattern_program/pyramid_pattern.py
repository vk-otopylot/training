num = int(input('Enter the number you want to see pyramid pattern: '))

#Using nested Loop

# for i in range(1, num+1):
#     for j in range(num-i):
#         print(' ', end='')
#     for k in range((i*2)-1):
#         print('*',end='')
#     print()

#Using range() function

for i in range(1,num+1):
    print(' ' * (num-i), end='')
    print('*' * ((i*2)-1))