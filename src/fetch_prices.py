import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("TWELVE_DATA_API_KEY")
params = {
    "symbol": "AAPL",
    "interval": "1day",
    "outputsize": 5,
    "apikey": api_key,
}
response = requests.get("https://api.twelvedata.com/time_series", params=params)
import pandas as pd

data = response.json()
df = pd.DataFrame(data["values"])
df["close"] = pd.to_numeric(df["close"])
df["open"] = pd.to_numeric(df["open"])
df["high"] = pd.to_numeric(df["high"])
df["low"] = pd.to_numeric(df["low"])
df["volume"] = pd.to_numeric(df["volume"])
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.reset_index(drop=True)



print(df.shape)
print(df.dtypes)