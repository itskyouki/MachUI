from modules import clock
import time
import json
from pathlib import Path

# data path
clock_file = Path(__file__).parent.parent / "data" / "clock.json"

# start up stuff
clock_info = clock.get_time()
with open(clock_file, "w") as clockfile:
    json.dump(clock_info, clockfile)
# loop stuff
current_time = time.time()
lu_clock = current_time

while True:
    current_time = time.time()
    if current_time - lu_clock >= 1:
        clock_info = clock.get_time()
        lu_clock = current_time
        with open(clock_file, "w") as clockfile:
            json.dump(clock_info, clockfile)
    time.sleep(0.1)