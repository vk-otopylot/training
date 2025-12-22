num = int(input('Enter the number you want to see diamond pattern: '))

for i in range(1, num+1):
    print(' ' * (num-i), end='')
    print('*' * ((i*2)-1))
for j in range(num-1,0,-1):
    print(' ' * (num-j), end='')
    print('*' * ((j*2)-1))