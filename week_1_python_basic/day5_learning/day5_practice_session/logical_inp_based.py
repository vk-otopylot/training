# Palindrome Check

# For Number

# value = int(input('Enter any Number to check whether it is palindrome or not: '))
# og = value
# res = 0
# while value > 0:
#     last = value % 10
#     res = (res * 10) + last
#     value = value // 10
#
# if og == res:
#     print('Palindrome')
# else:
#     print('Not Palindrome')


# For String

text = input('Enter any string to check whether is is palindrome or not: ')

res = text[::-1]

if res == text:
    print('Palindrome')
else:
    print('Not Palindrome')