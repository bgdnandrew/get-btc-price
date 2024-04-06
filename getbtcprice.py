import os
from dotenv import load_dotenv

import tweepy
import time
import requests

load_dotenv()

API_KEY             = os.getenv('API_KEY')
API_KEY_SECRET      = os.getenv('API_KEY_SECRET')
BEARER_TOKEN        = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN        = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# deprecated
# -----------------------------
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)
# -----------------------------

# new method according to tweepy 4.X
client = tweepy.Client(bearer_token = BEARER_TOKEN , 
                       consumer_key = API_KEY, 
                       consumer_secret = API_KEY_SECRET, 
                       access_token = ACCESS_TOKEN, 
                       access_token_secret = ACCESS_TOKEN_SECRET)

def get_btc_value():
    print("Getting BTC value from Coinbase")
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    print("Response: " + str(response.status_code) + " " + response.reason)
    data = response.json()
    cryptocurrency = data["data"]["base"]
    price = data["data"]["amount"]
    print ("Cryptocurrency: " +  cryptocurrency + " Price: " + price)

    # deprecated
    # api.update_status('#BTC is now at $' + price)

    # new method according to tweepy 4.X
    tweet_string = "#BTC is now at $" + price + " | via orientedplatforms.com"
    client.create_tweet(text = tweet_string)
    print("Tweeted: ", tweet_string)

while 1==1:
    print("Entered the continous loop")
    time.sleep(10)
    get_btc_value()
    print("Just tweeted, now sleeping for 25 minutes")
    time.sleep(1500)
    print("Woke up, now ready to tweet again")
