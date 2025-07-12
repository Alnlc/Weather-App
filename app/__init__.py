import requests

api_url = "https://api.openweathermap.org/data/3.0/onecall?lat={-16.3262}&lon={-48.9515}&appid={d3a661a2b87ef2a9a1b9e28c9e6c9dad}"

response = requests.get(api_url)
print (response)


