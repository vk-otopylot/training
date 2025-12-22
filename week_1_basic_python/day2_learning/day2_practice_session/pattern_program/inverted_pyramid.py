num = int(input('Enter the number you want to see inverted pyramid pattern: '))

#using range() function

# for i in range(num,0,-1):
#     print(' ' * (num-i),end='')
#     print('*' * ((i*2)-1))

#Using nested loop

for i in range(num, 0 , -1):
    for j in range(num-i):
        print(' ', end='')
    for k in range(i*2-1):
        print('*', end='')
    print()