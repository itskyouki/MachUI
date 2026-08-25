import requests
from pathlib import Path
import json

def get_weather():
    # data path
    weather_file = Path(__file__).parent.parent.parent / "data" / "weather.json"
# lat and long (replace with auto location)
    latitude =  78
    longitude = 78
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&daily=sunrise,sunset,uv_index_max,precipitation_probability_max"
        "&hourly=temperature_2m,precipitation_probability,apparent_temperature,wind_speed_10m,weather_code"
        "&timezone=Australia%2FSydney"
)
    response = requests.get(url)
    weather_info = response.json()
    print(weather_info)
    with open(weather_file, "w") as weatherfile:
        json.dump(weather_info, weatherfile)
    return weather_info

get_weather
