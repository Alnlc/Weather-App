from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
from os import getenv

load_dotenv()

API_KEY = getenv('KEY_API')
API_URL = "https://api.weatherbit.io/v2.0"

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/weathermap', methods = ['POST', 'GET'])
def weathermap():

    try:
        lat = request.args.get('lat')
        lon = request.args.get('lon')

    except Exception as e:
        print(f'error: {e}')
        
    def currentWeather():
        endpoint =  "/current"
        params = {
            "lat" : lat, 
            "lon" : lon,
            "lang" : "pt",
            "metric" : "M",
            "key" : API_KEY
        }
        fullUrl = f"{API_URL}{endpoint}"
        
        try:
            response = requests.get(fullUrl, params = params)
            response.raise_for_status()
            dataResponse = response.json()
            print(dataResponse)
            currentWeatherData = {
                'city' : dataResponse['city_name'],
                'country' : dataResponse['country_code'],
                'currentTemp' : dataResponse['data'][0]['temp'],
                'highTemp' : dataResponse['data'][0],
                'lowTemp' : dataResponse['data'][0],
                'time' : dataResponse['data'][0],
                'wind' : dataResponse['data'][0],
                'rh' : dataResponse['data'][0],
                'pod' : dataResponse['data'][0],
                'description' : dataResponse['data'][0]['weather']['description'],
                'icon' : dataResponse['data'][0]['weather']['icon']
            }

            #return jsonify(currentWeatherData.json())

        except Exception as e:
            print(f"Current weather request erro: {e}")

    def forecastWeather():
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
            forecastWeatherData = {
                'date' : dataResponse['data'][0]['datetime'],
                'highTemp' : dataResponse['data'][0]['high_temp'],
                'lowTemp' : dataResponse['data'][0]['low_temp'],
                'description' : dataResponse['data'][0]['weather']['description'],
                'icon' : dataResponse['data'][0]['weather']['icon']
            }
            print (forecastWeatherData)
            return jsonify(forecastWeatherData.json())

        except Exception as e:
            print(f"Forecast request erro: {e}")
    
    return render_template('weather.html', title='Weather')

