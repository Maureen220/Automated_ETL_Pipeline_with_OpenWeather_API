import datetime

import requests

from google.cloud import secretmanager
from posgresql_upload import upload_to_db


def get_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/weather-data-439820/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)
    secret = response.payload.data.decode("UTF-8")
    return secret


api_key = get_secret("weather_api_key")
today = str(datetime.datetime.today())


def import_current_weather():
    # API lat/long
    coordinates = {
        "denver": {"lat": "39.7392", "long": "-104.9903"},
        "salt lake city": {"lat": "40.7608", "long": "-111.8910"}
    }

    weather_data = []

    for city in coordinates:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[city]['lat']}" \
              f"&lon={coordinates[city]['long']}&appid={api_key}"

        params = {
            "units": "imperial"
        }

        request = requests.get(url, params=params).json()

        city_weather = request["main"]
        city_weather["city"] = city
        city_weather["datetime"] = today

        weather_data.append(city_weather)

    print(weather_data)
    upload_to_db(weather_data)
