import requests
from config import api_key
import pandas as pd


API_KEY = api_key
DENVER_LAT = "39.7392"
DENVER_LONG = "-104.9903"


def import_current_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={DENVER_LAT}&lon={DENVER_LONG}&appid={API_KEY}"
    params = {
        "units": "imperial"
    }

    request = requests.get(url, params=params)

    print(request.content)
