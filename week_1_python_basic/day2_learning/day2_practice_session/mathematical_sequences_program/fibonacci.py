number = int(input('Enter number you want see Fibonacci series: '))

a = 0
b = 1

if number == 1:
    print(a)

else:
    print(a)
    print(b)

    for i in range(2, number):
        c = a + b
        a = b
        b = c
        print(c)