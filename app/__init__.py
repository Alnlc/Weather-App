from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
from os import getenv

load_dotenv()

API_KEY = getenv('KEY_API')
API_URL = "https://api.weatherbit.io/v2.0"

def currentWeather(lat, lon):
    endpoint = "/current"
    params = {
        "lat": lat,
        "lon": lon,
        "lang": "pt",
        "metric": "M",
        "key": API_KEY
    }
    fullUrl = f"{API_URL}{endpoint}"

    try:
        response = requests.get(fullUrl, params=params)
        response.raise_for_status()
        data = response.json()['data'][0]
        print (data)
        currentWeatherData = {
            'city': data['city_name'],
            'country': data['country_code'],
            'currentTemp': data['temp'],
            'time': data['ob_time'],
            'wind': data['wind_spd'],
            'rh': data['rh'],
            'pod': data['pod'],
            'description': data['weather']['description'],
            'icon': data['weather']['icon']
        }
        return currentWeatherData
    except Exception as e:
        print(f"Current weather request erro: {e}")


def forecastWeather(lat, lon):
    endpoint = "/forecast/daily"
    params = {
        "lat": lat,
        "lon": lon,
        "days": 5,
        "lang": "pt",
        "metric": "M",
        "key": API_KEY
    }
    fullUrl = f"{API_URL}{endpoint}"

    try:
        response = requests.get(fullUrl, params=params)
        response.raise_for_status()
        dataResponse = response.json()

        fullForecast = []

        for day in dataResponse['data']:
            dayWeatherData = {
                'date': day['datetime'],
                'highTemp': day['high_temp'],
                'lowTemp': day['low_temp'],
                'description': day['weather']['description'],
                'icon': day['weather']['icon']
            }
            fullForecast.append(dayWeatherData)

        return fullForecast

    except Exception as e:
        print(f"Forecast request erro: {e}")

# Rio de Janeiro, Latitude: -22.9035, Longitude: -43.2096



print(forecastWeather(-22.9035,-43.2096))
print(currentWeather(-22.9035,-43.2096))