from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from os import getenv
import requests
import datetime



load_dotenv()

API_KEY = getenv('KEY_API')
API_URL = "https://api.weatherbit.io/v2.0"

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    now = datetime.datetime.now()
    print(now)
    if 6 <= now.hour <18 :
        return render_template('weather-day.html', title='Weather')
    else:
        return render_template('weather-nigth.html', title='Weather')
@app.route('/weathermap', methods = ['GET'])
def weathermap():
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

    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({'error': 'Os parametros "lat" e "lon" não foram cumpridos'}), 400
    
    responseData = {
        'current' : currentWeather(lat, lon),
        'forecast' : forecastWeather(lat, lon)
    }



    return jsonify(responseData)

if __name__ == '__main__':
    app.run(debug=True)