import requests

api_key = '9849492db19201fcec354b5216a8a0cd'

while True:
    user_input = input('Enter city (press Enter to exit): ').strip()

    if user_input == "":  
        print("Exiting program...")
        break

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}"
    )

    if weather_data.json().get('cod') == '404':
        print('No city found, please try again.\n')
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        print(f'The weather in {user_input} is {weather}')
        print(f'The temperature is {temp}°C\n')
