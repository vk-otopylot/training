first_no = int(input('Enter first number: '))
second_no = int(input('Enter first number: '))

operation = input('press \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n')

if operation == '1':
    result = first_no + second_no
    print('addition =', result)

elif operation == '2':
    result = first_no - second_no
    print('subtraction =', result)

elif operation == '3':
    result = first_no * second_no
    print('multiplication =', result)

elif operation == '4':
    result = first_no / second_no
    print('division =', result)

else:
    print('Invalid choice')