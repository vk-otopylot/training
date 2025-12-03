num = int(input('Enter the number you want to show reverse right angel star pattern: '))

# for i in range(1, num+1):
#     for j in range(num-i+1):
#         print("*", end='')
#     print()

for i in range(num, 0, -1):
    print('*' * i)