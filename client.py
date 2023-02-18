import requests, keyboard, time

# URL
url = 'http://localhost:5050/'

take_kettle = requests.get(url)
print(take_kettle.json().get('message'))

water_amount = input()
add_water = requests.post(url, json={'water_amount': water_amount})
# если error в ответе, то выходим из программы
if add_water.json().get('error'):
    print(add_water.json().get('error'))
    exit()
print(add_water.json().get('message'))

print('Нажмите "P" (Power) для включения/выключения чайника')
keyboard.wait('p')

print('Нажата клавиша "P", вода нагревается')
turning_on = requests.put(url)
print(turning_on.json().get('message'))

keyboard.add_hotkey('p', requests.delete(url))

turning_off = requests.delete(url)
print(turning_off.json().get('message'))
