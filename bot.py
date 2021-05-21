import tweepy, time, sys
from os import environ
import datetime as dt
from datetime import timedelta
from datetime import date

## Consts
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

## API Auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

### Main Function
hours = dt.datetime.now().hour;
date = dt.datetime.now();
timeZoneDelta = timedelta(hours = 3)
date -= timeZoneDelta;

tweetString = str(date.strftime("%d/%m/%y %H:%M"));
tweetString += "\nHora de coletar pontos no TheKKing, Once!";

if(hours == 13):
    tweetString += "\nNão se esqueça do Mubeat também, já passou 24h!";
    
hourToImgNumber = (hours % 8 + 1);
imagePath = "memes/"+ str(hourToImgNumber) + ".jpg";
    
api.update_with_media(imagePath, tweetString);