# Prints the weather for a location from the command line.

import json
import sys

import requests

APPID = '2bf847496feb86be8d37cc240df94331'

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: get_weather.py Bordeaux')
    sys.exit()
location = (sys.argv[1])

cities = {'Bordeaux' : {'lat' : '44.8378',  'lon' : '-0.594'}}


# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/weather?lat={cities[location]["lat"]}&lon={cities[location]["lon"]}&appid={APPID}&units=metric'
response = requests.get(url)
response.raise_for_status()

#Uncomment to see the raw JSON text:
#print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
main = weatherData['main']
weather = weatherData['weather']
print(f'Current weather in {location} : ')
print(f'{weather[0]["description"]}. The temperature is {main["temp"]}.')
