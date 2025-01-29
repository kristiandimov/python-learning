import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people currenly in space')
for people in json['people']:
    print(people['name'])
