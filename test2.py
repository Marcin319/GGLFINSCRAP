import requests
import pandas as pd
from datetime import datetime

symbol = "TSLA"
url = f"https://finance.google.com/finance/getprices?q={symbol}&i=86400&p=MAX&f=d,c,v"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
lines = response.text.splitlines()

# Znajdź początek danych
data_lines = [line for line in lines if not line.startswith(('#', 'EXCHANGE', 'MARKET', 'TIMEZONE_OFFSET', 'DATA'))]

dates, prices, volumes = [], [], []

base_timestamp = None

for line in data_lines:
    parts = line.split(',')
    if parts[0].startswith('a'):  # nowa baza timestamp
        base_timestamp = int(parts[0][1:])
        dates.append(datetime.utcfromtimestamp(base_timestamp))
    else:
        offset = int(parts[0])
        dates.append(datetime.utcfromtimestamp(base_timestamp + offset*86400))
    prices.append(float(parts[1]))
    volumes.append(int(parts[2]))

df = pd.DataFrame({'Date': dates, 'Price': prices, 'Volume': volumes})
print(df.head())