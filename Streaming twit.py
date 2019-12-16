import tweepy
from tweepy import OAuthHandler
import json
import time
import sys
import pandas as pd
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'PQzx2JmWS3kxFCZ4vjHp3SzCI'
consumer_secret = 'YFJs8IJKj0Sx9gjSIxxeUAuOa0tPoYHmLw51p8mRFtyxafF5aA'
access_token = '838007462817071105-KccYqMF5PcZo0XqH0HGIUeqwlYkeJjy'
access_secret = 'ZD90hvLFwDCYY93dmFMRYlfSoukb33h5TgJTh7O9kDwv9'



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(StreamListener):
 
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        created_at=all_data["created_at"]
        folowers=all_data["user"]["followers_count"]
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        #print(x.translate(non_bmp_map))
        t="streamouts.json"
        f = open(t,"a",encoding="utf-8")
        print(username.translate(non_bmp_map),tweet.translate(non_bmp_map),created_at,folowers,file=f)
        f.close()
        
        return True
 
    def on_error(self, status):
        print (status)
 
 
twitterStream = Stream(auth, MyListener())
twitterStream.filter(track=["#virat"])
