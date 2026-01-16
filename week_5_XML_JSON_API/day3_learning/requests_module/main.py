import requests

# Send a GET request to a public API and print: Status code, Response text

response = requests.get('https://open.er-api.com/v6/latest/USD')
# print(response.status_code)
# print(response.text)
# print(response.headers)

