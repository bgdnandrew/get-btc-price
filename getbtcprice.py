import os
from dotenv import load_dotenv

load_dotenv()

import tweepy
import time
import requests


API_KEY             = os.getenv('API_KEY')
API_SECRET_KEY      = os.getenv('API_SECRET_KEY')
BEARER_TOKEN        = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN        = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def get_btc():
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    data = response.json()
    currency = data["data"]["base"]
    price = data["data"]["amount"]
    print ("Currency: " +  currency + " Price: " + price)
    api.update_status('#BTC is now at $' + price)

while 1==1:
    time.sleep(10)
    get_btc()
    time.sleep(1200)
