import requests
from pathlib import Path
import json

def get_weather():
    # data path
    weather_file = Path(__file__).parent.parent.parent / "data" / "weather.json"
    with open("data/location.json", "r") as file:
        location_info = json.load(file)
        city = location_info["city"]
        country = location_info["country"]
        timezone = location_info["timezone"]
        latitude = location_info["latitude"]
        longitude = location_info["longitude"]
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&daily=sunrise,sunset,uv_index_max,precipitation_probability_max"
        "&hourly=temperature_2m,precipitation_probability,apparent_temperature,wind_speed_10m,weather_code"
        f"&timezone={timezone}"
)
    response = requests.get(url)
    weather_info = response.json()
    with open(weather_file, "w") as weatherfile:
        json.dump(weather_info, weatherfile)
    return weather_info


