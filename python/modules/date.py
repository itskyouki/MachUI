from datetime import datetime
from pathlib import Path
import json
def get_date():

    # data path
    date_file = Path(__file__).parent.parent.parent / "data" / "date.json"
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    date_info = {
        "year": year,
        "month": month,
        "day": day
    }
    with open(date_file, "w") as datefile:
        json.dump(date_info, datefile)

