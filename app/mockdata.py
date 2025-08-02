def mockCoordinateLat():
    lat = '-22.951927'
    return(lat)

def mockCoordinatesLon():
    lon = '-43.21048'
    return(lon)

def mockCurrentData():
    data = {
        'city':'Rio de Janeiro',
        'country': 'Br',
        'currentTemp': 34,
        'time': "2025-08-01 00:15",
        'wind': 5.85,
        'rh': 13,
        'description': 'Céu limpo',
        'icon': "c01n"
        }
    return(data)

def mockDataForecast():
    data = [
        {
        'date':  "2025-08-02",
        'highTemp': 25.4,
        'lowTemp': 16.7,
        'description': "Céu limpo",
        'icon': "c01d"
        },
        {
        'date':  "2025-08-03",
        'highTemp': 25.6,
        'lowTemp': 15.7,
        'description': 'Poucas nuvens',
        'icon': "c02d"
        },
        {
        'date':  "2025-08-04",
        'highTemp': 24.8,
        'lowTemp': 18.1,
        'description': "Poucas nuvens",
        'icon': "c02d"
        },
        {
        'date':  "2025-08-05",
        'highTemp': 22,
        'lowTemp': 19.4,
        'description': "Nuvens quebradas",
        'icon': "c03d"
        },
        {
        'date':  "2025-08-06",
        'highTemp': 22.5,
        'lowTemp': 18.5,
        'description': "Nublado",
        'icon': "c04d"
        }
    ]
    return(data)