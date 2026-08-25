import time
from modules import clock
from modules import battery
from modules import weather

# start up stuff
clock_info = clock.get_time()
battery_info = battery.get_battery()
weather_info = weather.get_weather()

# loop stuff
current_time = time.time()
lu_clock = current_time
lu_battery = current_time
lu_weather = current_time

#main data loop
while True:
    current_time = time.time()
    if current_time - lu_clock >= 1:
        clock_info = clock.get_time()
        lu_clock = current_time
    if current_time - lu_battery >= 4:
            battery_info = battery.get_battery()
            lu_battery = current_time
    if current_time - lu_weather >= 7200:
        weather_info = weather.get_weather()
        lu_weather = current_time
    time.sleep(0.1)