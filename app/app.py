from flask import Flask, render_template, request, jsonify
import requests
import os

OPENWEATHER_API_KEY = os.getenv('KEY_API')
OPENWEATHER_API_URL = "https://api.openweathermap.org/data/3.0/onecall"

app = Flask(__name__)

@app.route('/home')

def index():
    return render_template('home.html', title='Home')

@app.route('/weatherapp')
def weathermap():

    
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    dt = request.args.get('dt')

    if not lat and not lon:
        return ("error", 400)

    api_url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return jsonify(response.json())

    except Exception as e:
        print(f"erro: {e}")
    
    return render_template('weather.html', title='Weather')


if __name__ == '__main__':
    app.run(debug=True)