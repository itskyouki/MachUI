from datetime import datetime

def get_time():
    hour = datetime.now().strftime("%I")
    minute = datetime.now().minute
    second = datetime.now().second
    clock_info = {
        "hour": hour,
        "minute": minute,
        "second": second
    }
    return(clock_info)
get_time()
