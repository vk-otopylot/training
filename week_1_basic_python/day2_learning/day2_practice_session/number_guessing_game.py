DECIDED_NUMBER = 25

while True:
    number = int(input('Enter the number: '))

    if number > DECIDED_NUMBER:
        print('Lower number please')

    elif number < DECIDED_NUMBER:
        print('Grater number please')

    elif number == DECIDED_NUMBER:
        print('Congratulations!! you guess it correct')
        break
    else:
        print('Invalid choice')