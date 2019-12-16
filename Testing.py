import tweepy
from tweepy import OAuthHandler
import json
import pandas as pd
 
consumer_key = 'PQzx2JmWS3kxFCZ4vjHp3SzCI'
consumer_secret = 'YFJs8IJKj0Sx9gjSIxxeUAuOa0tPoYHmLw51p8mRFtyxafF5aA'
access_token = '838007462817071105-KccYqMF5PcZo0XqH0HGIUeqwlYkeJjy'
access_secret = 'ZD90hvLFwDCYY93dmFMRYlfSoukb33h5TgJTh7O9kDwv9'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


 
message,created_at=[],[]
for tweet in tweepy.Cursor(api.user_timeline).items(1):
    message.append(tweet.text)
    created_at.append(tweet.created_at)
    
df=pd.DataFrame({'Message':message,
                'Create At':created_at})
df.to_csv("my tweets.csv")
print("\n\nNEW\n\n",df)
