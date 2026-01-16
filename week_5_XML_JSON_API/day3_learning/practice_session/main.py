import requests
import json

# Fetch list of users from a public API and store it in a JSON file.
#
# response = requests.get('https://jsonplaceholder.typicode.com/users')
#
# data = json.dumps(response.json(), indent = 4)
#
# with open('users.json', 'w') as file:
#     file.write(data)


# post the requests with data

data = {
    'name': 'vivek',
    'age': 21
}

r = requests.post('https://jsonplaceholder.typicode.com/posts', data= data)
print(r)