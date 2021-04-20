import tweepy, time, sys
from os import environ
import datetime as dt

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


while(True):
    if(dt.datetime.now().minute == 0):
        api.update_status("Vai votar!")
        time.sleep(60)
    else:
        api.update_status("Não vai votar!")
        time.sleep(60)