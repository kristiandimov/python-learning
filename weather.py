import requests

city = 'Plovdiv'
url = 'http://api.weatherapi.com/v1/current.json?key=3e0c5afe16374f0e9f2101612240409&q='+ city +'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in",city,'is',description,'and',temp,'degrees')