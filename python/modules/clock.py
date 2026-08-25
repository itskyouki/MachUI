from datetime import datetime
import json
from pathlib import Path
def get_time():
    # data path
    clock_file = Path(__file__).parent.parent.parent / "data" / "clock.json"

    hour = int(datetime.now().strftime("%I"))
    minute = datetime.now().minute
    second = datetime.now().second
    clock_info = {
        "hour": hour,
        "minute": minute,
        "second": second
    }
    with open(clock_file, "w") as clockfile:
                json.dump(clock_info, clockfile)
    return(clock_info)
