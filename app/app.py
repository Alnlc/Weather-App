from flask import Flask, render_template, request, jsonify
import requests
from app.key_app import keyW

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Weather')

@app.route('/app/weathermap/')
def weathermap():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    dt = request.args.get('dt')

    key = keyW()
    if not lat and not lon:
        return ("error", 400)

    api_url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={key}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return jsonify(response.json())

    except Exception as e:
        print(f"erro: {e}")

if __name__ == '__main__':
    app.run(debug=True)