import tweepy, time, sys
import datetime as dt
from datetime import timedelta
from datetime import date


"""CONSUMER_KEY = '1TdfPV8Sj531oqgZu2cslOuSm'
CONSUMER_SECRET = 'T729YIG6LExWtnkN9n5kL3cJuw9kTs3xkU2wUIP6UrUnDwDpmp'
ACCESS_KEY = '1384374470828298242-dRBJMuKdsBis6Cy5qoEDgxpDJROD1R'
ACCESS_SECRET = 'sRJDlLKdookcaV0o86OLkCnGSO3AgHXX40sg9SVO8i6si'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)"""

### Main Function
hours = dt.datetime.now().hour;
date = dt.datetime.now();
timeZoneDelta = timedelta(hours = 3)
date -= timeZoneDelta;

tweetString = str(date.strftime("%d/%m/%y %H:%M"));
tweetString += "\nHora de coletar pontos no TheKKing, Once!";

if(hours == 13):
    tweetString += "\nNão se esqueça do Mubeat também, já passou 24h!";

if((hours % 2) == 0):
    imagePath = "1.jpg";
else:
    imagePath = "2.jpg";

print(tweetString, imagePath);
## api.update_with_media(imagePath, tweetString)