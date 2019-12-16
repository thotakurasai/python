import tweepy
from tweepy import OAuthHandler
import json
import time
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
        try:
            with open('sachin.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#sachin'])
