age = int(input('Enter your age: '))

if age >= 18:
    if age >=60:
        print('Senior voter')
    else:
        print('Adult voter')
else:
    print('Not eligible')