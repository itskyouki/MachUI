import clock
import time
# start up stuff
clock_info = clock.get_time

# loop stuff
current_time = time.time()
lu_clock = current_time

while True:
    current_time = time.time()
    if current_time - lu_clock >= 1:
        clock_info = clock.get_time()
        lu_clock = current_time
        print(clock_info)

    time.sleep(0.1)