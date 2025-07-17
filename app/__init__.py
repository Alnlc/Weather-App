from dotenv import load_dotenv
import requests
from os import getenv
import json

load_dotenv()

API_KEY = getenv('KEY_API')
API_URL = "https://api.weatherbit.io/v2.0"

def forecastWeather(lat, lon):
    endpoint = "/forecast/daily"
    params = {
            "lat" : lat, 
            "lon" : lon,
            "days" : 5,
            "lang" : "pt",
            "metric" : "M",
            "key" : API_KEY
        }
    fullUrl = f"{API_URL}{endpoint}"
    
    try:
    
        response = requests.get(fullUrl, params = params)
        response.raise_for_status()
        dataResponse = response.json()

        fullForecast = []

        for day in dataResponse['data']:
        
            dayWeatherData = {
                'date' : day['datetime'],
                'highTemp' : day['high_temp'],
                'lowTemp' : day['low_temp'],
                'description' : day['weather']['description'],
                'icon' : day['weather']['icon']
                }
            fullForecast.append(dayWeatherData)
        
        return fullForecast
    except Exception as e:
        print(f"Forecast request erro: {e}")

v = forecastWeather(-16.3295037, -48.9706901)
print(v)