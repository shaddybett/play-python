import requests

response = requests.get('https://randomuser.me/api')
gender = response.json()['results'][0]['gender']
title = response.json()['results'][0]['name']['title']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
print(f'{title}. {first_name} {last_name} {gender}')
