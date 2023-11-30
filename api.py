import requests

response = requests.get('https://randomuser.me/api')
print(response.json())
print(response.status_code)