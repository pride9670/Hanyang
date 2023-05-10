#!/usr/bin/env python3


import requests
import pandas as pd
import time
import datetime


now = datetime.datetime.now()
print(f"시작시간: {now}")

while now.second!=0 or now.minute!=0 or now.hour!=0:
    
    book = {}
    
    response = requests.get('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=5')
    
    book = response.json()
    
    data = book['data']
    bids = (pd.DataFrame(data['bids'])).apply(pd.to_numeric, errors='ignore')
    bids.sort_values('price', ascending=False, inplace=True)
    bids = bids.reset_index(); del bids['index']
    bids['type'] = 0
    
    asks = (pd.DataFrame(data['asks'])).apply(pd.to_numeric, errors='ignore')
    asks.sort_values('price', ascending=True, inplace=True)
    asks['type'] = 1
    
    df = pd.concat([bids, asks])
    df['quantity'] = df['quantity'].round(decimals=4)
    timestamp = datetime.datetime.now()
    df['timestamp'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    print(df)
    df.to_csv('./2023-05-09-bithumb-orderbook.csv', index=False, header=False, mode='a')
    time.sleep(1)
else : print("2023.05.09 orderbook 생성완료")
    
 
