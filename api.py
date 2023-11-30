import requests

response = requests.get('https://randomuser.me/api')
print(response.json())
print(response.status_code)
gender = response.json()['results'][0]['gender']
title = response.json()['results'][0]['name']['title']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
print(f'{title}. {first_name} {last_name} {gender}')