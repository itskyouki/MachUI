from pathlib import Path
import json
import subprocess

def get_battery():
    # data path
    battery_file = Path(__file__).parent.parent.parent / "data" / "battery.json"
    power_supply = Path("/sys/class/power_supply")
    #try to find battery
#    for path in power_supply.iterdir():
#        if path.name.startswith("BAT"):

    #search for battery stuff
    result = subprocess.run(["cat","/sys/class/power_supply/BAT0/capacity"],capture_output=True,text=True)
    bat_cap = int(result.stdout.strip())
    result = subprocess.run(["cat","/sys/class/power_supply/BAT0/status"],capture_output=True,text=True)
    bat_stat = result.stdout.strip() 
    result = subprocess.run(["cat","/sys/class/power_supply/BAT0/health"],capture_output=True,text=True)
    bat_health = result.stdout.strip()
    result = subprocess.run(["cat","/sys/class/power_supply/BAT0/voltage_now"],capture_output=True,text=True)
    bat_volt = int(result.stdout.strip()) / 1000000
    result = subprocess.run(["cat","/sys/class/power_supply/BAT0/current_now"],capture_output=True,text=True)
    bat_current = int(result.stdout.strip()) / 1000000
    bat_watt = bat_current * bat_volt
    #dictionary
    battery_info = {
            "capacity": bat_cap,
            "status": bat_stat,
            "health": bat_health,
            "voltage": bat_volt,
            "current": bat_current,
            "wattage": bat_watt
        }
    #return and json dump
    with open(battery_file, "w") as batteryfile:
                    json.dump(battery_info, batteryfile)
    return(battery_info)
