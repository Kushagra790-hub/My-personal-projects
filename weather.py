import requests


city_name = input("Enter your city name: ")
API_key = '7cbf33ac0c0f0d6e57ad3246bf192361'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

respone = requests.get(url) 
if respone.status_code == 200:
    data = respone.json()
    print('Weather is: ',data['weather'][0]['description'])
    print('Current temprature is: ',data['main']['temp'])
    print('Current temprature feels like is: ',data['main']['feels_like'])
    print('Humidity is: ',data['main']['humidity'])

else:
    print("Type the right city name. ")