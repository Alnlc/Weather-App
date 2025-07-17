from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
from os import getenv

load_dotenv()

API_KEY = getenv('KEY_API')
API_URL = "https://api.weatherbit.io/v2.0"

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('weather.html', title='Weather')
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
            dataResponse = response.json()
            print(dataResponse)
            currentWeatherData = {
                'city': dataResponse['city_name'],
                'country': dataResponse['country_code'],
                'currentTemp': dataResponse['data'][0]['temp'],
                'time': dataResponse['data'][0]['ob_time'],
                'wind': dataResponse['data'][0]['wind_spd'],
                'rh': dataResponse['data'][0]['rh'],
                'pod': dataResponse['data'][0]['pod'],
                'description': dataResponse['data'][0]['weather']['description'],
                'icon': dataResponse['data'][0]['weather']['icon']
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
        'forecast' : forecastWeather(lat, lon),
    }



    return jsonify(responseData)

if __name__ == '__main__':
    app.run(debug=True)