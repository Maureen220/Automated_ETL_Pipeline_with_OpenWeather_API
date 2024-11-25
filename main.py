import datetime

import requests

from config import api_key
from posgresql_upload import upload_to_db

API_KEY = api_key
TODAY = str(datetime.datetime.today())


def import_current_weather():
    # API lat/long
    coordinates = {
        "denver": {"lat": "39.7392", "long": "-104.9903"},
        "salt lake city": {"lat": "40.7608", "long": "-111.8910"}
    }

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
        city_weather["datetime"] = TODAY

        weather_data.append(city_weather)

    print(weather_data)

    upload_to_db(weather_data)
