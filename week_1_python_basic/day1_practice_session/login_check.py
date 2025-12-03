CORRECT_USERNAME = 'vivek'
CORRECT_PASSWORD = 'Vivek@123'

username = input('enter your username: ')
password = input('enter your password: ')

if not username or not password:
    print('both field required')

elif username != CORRECT_USERNAME and password != CORRECT_PASSWORD:
    print('invalid credential')

elif username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
    print('login successfully')

else:
    print('Invalid option')