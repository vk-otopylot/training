num = int(input('Enter the number you want to show inverted pyramid pattern: '))

for i in range(1,num+1):
    print(' ' * (i-1))
    print('*' * (num-i+1))