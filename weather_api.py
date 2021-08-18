#weather API
import requests


def format_response(weather_json):
   # format json data of weather
   try:
      city_name       = weather_json['name']
      condition       = weather_json['weather'][0]['description']
      temparature     = weather_json['main']['temp']
      icon_name       = weather_json['weather'][0]['icon']
      weather_report    = 'City: %s \nCondition: %s \nTemperature (°F): %s' % (city_name, condition, temparature)
   except:
      weather_report = 'OOPS!, Failed to retrieving informations'
      icon_name = ''
   return (weather_report, icon_name)


def weather_information(city_name):
# get Weather information bt calling openweathermap api

   weather_key = 'a036e0fc9e33d76f46e02a74b7b85373'
   url = 'https://api.openweathermap.org/data/2.5/weather'
   params = {'APPID': weather_key, 'q':city_name, 'units': 'imperial'}
   response = requests.get(url, params)
   weather_data = response.json()
   weather_report = format_response(weather_data)
   return weather_report

#print(weather_information('Dhaka'))
