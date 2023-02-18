import requests

# URL
url = 'http://localhost:5050/'

take_kettle = requests.get(url)
print(take_kettle.json().get('message'))

water_amount = input()
put_water = requests.put(url, json={'water_amount': water_amount})
print(put_water.json().get('message'))