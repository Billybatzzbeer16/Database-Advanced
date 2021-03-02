from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import pymongo as mongo
import redis

r = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8" ,decode_responses=True)

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bitcoin"]
mycol = mydb["Values"]

def parser():
  
    hash = r.lrange("hash", 0, 1000)
    time = r.lrange("tijd", 0, 1000)
    btc = r.lrange("btc", 0, 1000)
    usd = r.lrange("usd", 0, 1000)    

    data = {
        'Hash' : hash,
        'Time' : time,
        'Amount BTC' : btc,
        'Amount USD' : usd
    }
    df = pd.DataFrame(data)
    df = df.sort_values(by=['Amount BTC'], ascending = False)
    df = df.head(1)

    arr = df.columns
    mydict = {}

    lijst = df.stack().tolist()
    for x in range(len(lijst)):
        mydict[arr[x]] = lijst[x]

    x = mycol.insert_one(mydict)  


while True:
    parser()
    time.sleep(60)
      
