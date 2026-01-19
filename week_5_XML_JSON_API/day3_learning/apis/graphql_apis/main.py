
import requests

url = "https://countries.trevorblades.com/graphql"

body = """
query($code: ID!) {
    country(code: $code){
        name
        languages{
            name
        }
    }
}
"""
variables =  {
   "code": "DE"
}

print(url)
print(body)

response = requests.post(url=url, json={"query": body, "variables": variables})
print("response status code: ", response.status_code)
print(response.headers)
print(response.json())
if response.status_code == 200:
    print("response : ", response.content)