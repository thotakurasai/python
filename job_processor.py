def lambda_handler(event, context):
    print("=== Start parsing AWS schedule.")
    # print("event: ", event)
    # print('eventbody: ', event.get('Records')[0]['body'])
    hash_tags = event.get('Records')[0]['body']
    # print("eventtype: ", type(event.get('Records')[0]))
    hash_tag_list = hash_tags.split(',')
    print(hash_tag_list)


    from tweepy import API
    from tweepy import Cursor
    from tweepy.streaming import StreamListener
    from tweepy import OAuthHandler
    from tweepy import Stream

    from textblob import TextBlob

    import config

    import numpy as np
    import pandas as pd
    import re
    import json
    import tempfile
    import boto3

    # # # # TWITTER CLIENT # # # #
    class TwitterClient():
        def __init__(self):
            # print("TwitterClient")
            self.auth = TwitterAuthenticator().authenticate_twitter_app()

        def get_tweet_based_on_hashtag(self, hashtag_list):
            # print("get_tweet_based_on_hashtag")
            tweets = []
            self.api = API(self.auth, wait_on_rate_limit=True)
            for tweet in Cursor(self.api.search, q=hashtag_list, count=100,  lang="en").items():
                tweets.append(tweet)
            # print(len(tweets))
            # print(tweets[1])
            # with open('stream-data.json', 'w') as outfile:
            #     outfile.write('***'.join(tweets))
            return tweets


    # # # # TWITTER AUTHENTICATER # # # #
    class TwitterAuthenticator():

        def authenticate_twitter_app(self):
            # print("TwitterAuthenticator: authenticate_twitter_app")
            auth = OAuthHandler(config.TWITTER_CONSUMER_KEY,
                                config.TWITTER_CONSUMER_SECRET)
            auth.set_access_token(config.TWITTER_ACCESS_TOKEN,
                                config.TWITTER_ACCESS_TOKEN_SECRET)
            return auth


    class TweetAnalyzer():
        """
        Functionality for analyzing and categorizing content from tweets.
        """

        def clean_tweet(self, tweet):
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

        def tweets_to_data_frame(self, tweets):
            df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

            df['id'] = np.array([tweet.id for tweet in tweets])
            df['len'] = np.array([len(tweet.text) for tweet in tweets])
            df['date'] = np.array([tweet.created_at for tweet in tweets])
            df['source'] = np.array([tweet.source for tweet in tweets])
            df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
            df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

            return df

    def upload_in_s3(filename, bucketname):
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file('/tmp/' + filename, bucketname, filename)
        print("file uploaded successfully")

    create_sentiment()

    return None

