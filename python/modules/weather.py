import requests
from pathlib import Path
import json

def get_weather():
    # data paths
    data_dir = Path(__file__).parent.parent.parent / "data"
    weather_file = data_dir / "weather.json"
    location_file = data_dir / "location.json"

    with open(location_file, "r") as file:
        location_info = json.load(file)

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


