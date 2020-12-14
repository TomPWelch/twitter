#Getting all needed packages and credentials

import datetime
import tweepy
import pandas as pd
import time
import pip
from random import randint
from time import sleep

#adding all the keys/secrets etc for my app in twitter

consumer_key = '' 
consumer_secret = '' 
access_token = '-' 
access_token_secret = '' 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



#Pulling all my tweets
d = pd.DataFrame()

for tweets in tweepy.Cursor(api.search,
                        q="😭 newborn sleep",
                        rpp=1000,
                        #geocode="51.5074,0.1278, 330km",
                        result_type="recent",
                        #source = "Twitter For Web",
                        include_entities=True,
                        lang="en").items(1000):

                        temp = pd.DataFrame(
                        {
                            'text': tweets.text,
                            'name': tweets.user.screen_name,
                            'created': tweets.created_at,
                            'tweet_id': tweets.id
                        },
                            index=[0]                 
    )
                        d = pd.concat([d, temp])


d2 = pd.DataFrame()

for tweets in tweepy.Cursor(api.search,
                        q="newborn sleep baby",
                        rpp=1000,
                        #geocode="51.5074,0.1278, 330km",
                        result_type="recent",
                        #source = "Twitter For Web",
                        include_entities=True,
                        lang="en").items(500):

                        temp = pd.DataFrame(
                        {
                            'text': tweets.text,
                            'name': tweets.user.screen_name,
                            'created': tweets.created_at,
                            'tweet_id': tweets.id
                        },
                            index=[0]                 
    )
                        d2 = pd.concat([d2, temp])


d.count() + d2.count()

result = [d, d2]
result = pd.concat(result)
#removing duplicates so I don't spam anyone
new_tweets = result[['name', 'tweet_id', 'created']]
new_tweets = new_tweets.drop_duplicates("name", keep='first')

#get the list of everyone
twitter_list = pd.read_csv('twitter_list.csv')
frames = [new_tweets, twitter_list]
all_tweets = pd.concat(frames)
all_tweets = all_tweets.drop_duplicates("name", keep='first')
all_tweets.to_csv(r'twitter_list.csv', index = False, float_format='%f')



#get the list of everyone
twitter_list = pd.read_csv('twitter_list.csv')
frames = [new_tweets, twitter_list]
all_tweets = pd.concat(frames)
all_tweets = all_tweets.drop_duplicates("name", keep='first')
all_tweets.to_csv(r'twitter_list.csv', index = False, float_format='%f')



            
      
