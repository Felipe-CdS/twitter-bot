import tweepy, time, sys
from os import environ
import datetime as dt

## Consts
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
imagePath = "img.jpg";

## API Auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

###Main Function
hours = dt.datetime.now().hour;
minutes = dt.datetime.now().minute;
if(minutes < 10):
    minutes = "0" + str(minutes);
if(hours < 0):
    hours = 24 - hours;

tweetString = dt.datetime.now().strftime("%d/%m/%Y ");
tweetString += str(hours-3) + ":" + str(minutes);
tweetString += "\nHora de coletar pontos no TheKKing, Once!";

if(dt.datetime.now().hour == 13):
    tweetString += "\nNão se esqueça do Mubeat também, já passou 24h!";

api.update_with_media(imagePath, tweetString);