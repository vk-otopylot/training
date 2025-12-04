name = input('Enter your name to check it is palindrome or not: ')

reverse = name[::-1]

if name == reverse:
    print('Palindrome')
else:
    print('Not Palindrome')