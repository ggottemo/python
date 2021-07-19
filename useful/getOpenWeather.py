#! python3
#getOpenWeather.py - Prints  the weather for a location from the command line

APPID = 'f3169602d09961a88d20e6e8a329ff19'

import json, requests, sys

#compute location from command line arguments.

if len(sys.argv )< 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ''.join(sys.argv[1:])

#Download the JSON data from OpenWeatherMap.org's API 




#Load JSON data into a python variable
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s'\
    %(location, APPID)
response = requests.get(url)
response.raise_for_status()

#Below comment lets you see raw JSON 
#print(response.text)

#Load JSON data into a Python variable

weatherData = json.loads(response.text)

#Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])