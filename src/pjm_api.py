import pandas as pd
import requests, os
from dotenv import load_dotenv
from datetime import datetime,timedelta
from src.db import engine
import json

load_dotenv()

url="https://api.pjm.com/api/v1/hrl_load_metered"
headers={
    "Ocp-Apim-Subscription-Key": os.getenv("PJM_API_KEY")
}

two_day_earlier=datetime.now()-timedelta(days=2)
date=two_day_earlier.strftime("%Y-%m-%d")

params={
    "rowCount": 50000,
    "startRow": 10,
    "datetime_beginning_utc": f"{date} 00:00 to {date} 01:59"

}
response = requests.get(
    url,
    headers=headers,
    params=params
)

response.raise_for_status()

response_json=response.json()

data=pd.DataFrame(response_json['items'])

print(data)


