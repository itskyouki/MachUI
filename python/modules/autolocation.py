import json
import urllib.request
from pathlib import Path

def get_location():
# data path
    location_file = Path(__file__).parent.parent.parent / "data" / "location.json"
    with urllib.request.urlopen("https://ipwho.is/", timeout=5) as response:
        data = json.load(response)
#returning dictionary
    location_info = {
    "city": data["city"],
    "country": data["country"],
    "timezone": data["timezone"]["id"],
    "latitude": data["latitude"],
    "longitude": data["longitude"]
}
#return and json dump
    with open(location_file, "w") as locationfile:
        json.dump(location_info, locationfile)
    return location_info

get_location()

