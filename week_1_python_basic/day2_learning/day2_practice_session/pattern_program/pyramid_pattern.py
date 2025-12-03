num = int(input('Enter the number you want to show pyramid pattern: '))

# for i in range(1, num+1):
#     for j in range(num-i):
#         print(' ', end='')
#     for k in range((i*2)-1):
#         print('*',end='')
#     print()

for i in range(1,num+1):
    print(' ' * (num-i), end='')
    print('*' * ((i*2)-1))