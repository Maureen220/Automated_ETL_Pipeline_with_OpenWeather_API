import requests
from config import api_key
import pandas as pd


API_KEY = api_key

coordinates = {
    "denver": {"lat": "39.7392", "long": "-104.9903"},
    "salt lake city": {"lat": "40.7608", "long": "-111.8910"}
}


def import_current_weather():
    weather_data = []

    for city in coordinates:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[city]['lat']}" \
              f"&lon={coordinates[city]['long']}&appid={API_KEY}"

        params = {
            "units": "imperial"
        }

        request = requests.get(url, params=params).json()

        city_weather = request["main"]
        city_weather["city"] = city

        weather_data.append(city_weather)

    df = pd.DataFrame(weather_data)
    return df


import_current_weather()
