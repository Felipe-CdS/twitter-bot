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

imagePath = "img.jpg";
tweetString = dt.datetime.now().strftime("%x %X");
tweetString += "\nHora de coletar pontos no TheKKing, Once!";

if(dt.datetime.now().hour == 13):
    tweetString += "\nNão se esqueça do Mubeat também, já passou 24h!";

api.update_with_media(imagePath, tweetString);