import requests

api_key = '9849492db19201fcec354b5216a8a0cd'

user_input = input('Enter city: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
#använder request library för att hämta url och det som finns i den spara i denna variabel 

#print(weather_data.status_code) för att testa om url fungerar 

#print(weather_data.json()) får all data som finns om vädret i json format

if weather_data.json()['cod'] == '404':
    print('No city found')
else: 
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f'The weather in {user_input} is {weather}')
    print(f'The temperature is {temp}°C')