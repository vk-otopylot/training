char = input('Enter any character: ')

if char.isalpha():
    char.lower()
    if char in 'a,e,i,o,u':
        print('Vowels ')
    else:
        print('consonants')

if char.isdigit():
    char = int(char)
    if char%2 == 0:
        print('Even')
    else:
        print('odd')

else:
    print('special symbol')