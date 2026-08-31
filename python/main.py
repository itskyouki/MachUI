import time
from modules import clock
from modules import battery
from modules import weather
from modules import autolocation
from modules import date
import shutil
from pathlib import Path
#startup
data_dir = Path(__file__).parent.parent / "data"

if not data_dir.exists():
    data_dir.mkdir()

shutil.rmtree(data_dir)
data_dir.mkdir()
autolocation.get_location()
clock.get_time()
battery.get_battery()
date.get_date()
weather.get_weather()

# loop stuff
current_time = time.time()
lu_clock = current_time
lu_battery = current_time
lu_weather = current_time
lu_location = current_time
lu_date = current_time

#main data loop
while True:
    current_time = time.time()

    if current_time - lu_clock >= 1:
        clock.get_time()
        lu_clock = current_time

    if current_time - lu_battery >= 4:
        battery.get_battery()
        lu_battery = current_time

    if current_time - lu_weather >= 7200:
        weather.get_weather()
        lu_weather = current_time

    if current_time - lu_location >= 3600:
        autolocation.get_location()
        lu_location = current_time
   if current_time - lu_date >= 86400:
        date.get_date()
        lu_date = current_time
