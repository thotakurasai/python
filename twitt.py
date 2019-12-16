import tweepy
from tweepy import OAuthHandler
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil import parser
import cmath
import math
from math import log
import numpy as np
import boto3
import boto


import collections
from collections import Counter


import gensim
import pkgutil
modules = pkgutil.iter_modules(gensim.__path__)
for module in modules:
    print(module[1])

from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

from nltk.stem.porter import *
stemmer = PorterStemmer()

 
consumer_key = 'PQzx2JmWS3kxFCZ4vjHp3SzCI'
consumer_secret = 'YFJs8IJKj0Sx9gjSIxxeUAuOa0tPoYHmLw51p8mRFtyxafF5aA'
access_token = '838007462817071105-KccYqMF5PcZo0XqH0HGIUeqwlYkeJjy'
access_secret = 'ZD90hvLFwDCYY93dmFMRYlfSoukb33h5TgJTh7O9kDwv9'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



keywords=["Crude Oil", "ARAMCO", "SAUDI", "Middle-East", "RIYAL", "Mohammed Al-Jadaan", "Saudi GDP", "Saudi Economy", "Saudi Exports", "Saudi UnEmployment"] 

message,valid_data,collect,favorite_count,tweet_count,retweet_count,created_at,user_name,verified,followers_count,following_count,days=[],[],[],[],[],[],[],[],[],[],[],[]


for keyword in range (len(keywords)):
    
    tweets = tweepy.Cursor(api.search,q=keywords[keyword]+" -filter:retweets", lang = 'en'
                        #since="2019-09-19",
                        #until="2019-09-20"
                        ).items(298)




    today = datetime.now()
    DD = timedelta(days=30)
    earlier = today - DD
    earlier_str = earlier.strftime("%Y-%m-%d %H:%M:%S")

    endDate = datetime(2019, 9, 20)
    count = 0


    """        def lemmatize_stemming(message):
                return stemmer.stem(WordNetLemmatizer().lemmatize(message, pos='v'))        
            for token in gensim.utils.simple_preprocess(tweet.text) :
                if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                    tlmessage.append(lemmatize_stemming(token))"""


    
    for tweet in tweets:
        #if tweet.created_at < endDate:
            message.append(tweet.text)
            favorite_count.append(tweet.favorite_count)
            retweet_count.append(tweet.retweet_count)
            created_at.append(tweet.created_at)
            user_name.append(tweet.user.name)
            verified.append(tweet.user.verified)
            a=tweet.user.id
            tweet_count.append(api.get_user(a).statuses_count)
            followers_count.append(tweet.user.followers_count)
            following_count.append(tweet.user.friends_count)
            
            def lemmatize_stemming(text):
                return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
            hello=[]
            for token in gensim.utils.simple_preprocess(tweet.text) :
                if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                    hello.append(lemmatize_stemming(token))

            collect.append(collections.Counter(hello))
            valid_data.append(hello)
            
            results = api.user_timeline(id=a, count=1)
            
            for tweet in results:
                create = tweet.created_at
                v=today-create
                """print(today  )
                print("my out")
                print(create )
                print(v.days)"""
                days.append(v.days)



            count = 0
            
    """        results = api.user_timeline(id=a, since="2019-10-01")
            
            for tweet in results:
                count = count + 1
                #print(count)
                
            last20_days.append(count)


            dayss=[i+1 for i in days]
            first= [x/y for x, y in zip(tweet_count, dayss)]
            followers_countt=[i+1 for i in followers_count]
            
            second=[math.log(y,10) for y in followers_countt]

            following_countt=[i+1 for i in following_count]
            third=[k/l for k, l in zip(followers_countt, following_countt)]
            thirdd=[j+1 for j in third]
            fourth=[math.log(z,10) for z in thirdd]
            final1=[a*b for a,b in zip(first,second)]
            final = [a*b for a,b in zip(final1,fourth)]
            influence.append(final)
        

        if(earlier_str < create):
                print('true')
        
        year2,month2,date2=tweet.created_at .split('-')
        """
        
        




    new_final_list = [] 
    for num in message: 
        if num not in new_final_list: 
            new_final_list.append(num)



        
    df=pd.DataFrame({'Message':new_final_list,
                     'valid_data':valid_data,
                     'collect':collect,
                    'Favourite Count':favorite_count,
                     'tweet_count':tweet_count,
                    'Retweet Count':retweet_count,
                    'Created At':created_at,
                    'user_name':user_name,
                     'verified':verified,
                     'followers count':followers_count,
                     'following count':following_count,
                     'days':days
                     #'last20_days':last20_days
                     #'influence':influence
                     })

    df.to_csv("Saudi Normal.csv")
    print(df)

t="Saudi Normal.csv"


bucketName = "test-bucket-saikiran"
Key = t
outPutname = t

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

