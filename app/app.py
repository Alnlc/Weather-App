from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from os import getenv
import requests
import datetime
import mockdata

load_dotenv()

API_KEY = getenv('KEY_API')
API_URL = "https://api.weatherbit.io/v2.0"

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    now = datetime.datetime.now()
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
                'description': data['weather']['description'],
                'icon': data['weather']['icon']
            }
            return currentWeatherData
        except Exception as e:
            print(f"Current weather request erro: {e}")
            currentWeatherData = mockdata.mockCurrentData()
            return currentWeatherData

    def forecastWeather(lat, lon):
        endpoint = "/forecast/daily"
        params = {
            "lat": lat,
            "lon": lon,
            "days": 10,
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
                date1 = str(datetime.date.today() + datetime.timedelta(days=2))
                date2 = str(datetime.date.today() + datetime.timedelta(days=3))
                date3 = str(datetime.date.today() + datetime.timedelta(days=4))
                date4 = str(datetime.date.today() + datetime.timedelta(days=5))
                date5 = str(datetime.date.today() + datetime.timedelta(days=6))
                if day['datetime'] == date1  or day['datetime'] == date2 or day['datetime'] == date3 or day['datetime'] == date4 or day['datetime'] == date5 :
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
            fullForecast = mockdata.mockDataForecast()
            return fullForecast

    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        
        lat = mockdata.mockCoordinateLat()
        lon = mockdata.mockCoordinatesLon()
        return jsonify({'error': 'Os parametros "lat" e "lon" não foram cumpridos, exibindo informações ficticias.'}), 400
    
    responseData = {
        'current' : currentWeather(lat, lon),
        'forecast' : forecastWeather(lat, lon)
    }



    return jsonify(responseData)

if __name__ == '__main__':
    app.run(debug=True)