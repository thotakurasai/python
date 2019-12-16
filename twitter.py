import tweepy
import sys
import json
from tweepy.auth import OAuthHandler
import pandas as pd
from bs4 import BeautifulSoup
 
consumer_key = 'PQzx2JmWS3kxFCZ4vjHp3SzCI'
consumer_secret = 'YFJs8IJKj0Sx9gjSIxxeUAuOa0tPoYHmLw51p8mRFtyxafF5aA'
access_token = '838007462817071105-KccYqMF5PcZo0XqH0HGIUeqwlYkeJjy'
access_secret = 'ZD90hvLFwDCYY93dmFMRYlfSoukb33h5TgJTh7O9kDwv9'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# The search term you want to find
query = "Kohli"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)



# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    #print(x.translate(non_bmp_map))
    t="twitteroutputs.csv"
    f = open(t,"a",encoding="utf-8")
    print (tweet.user.screen_name,"Tweeted:",tweet.text.translate(non_bmp_map),file=f)
    f.close()
"""
for status in tweepy.Cursor(api.home_timeline).items(50):
    
    u=status.text
    u=u.encode('unicode-escape').decode('utf-8')
    print(u)
"""
