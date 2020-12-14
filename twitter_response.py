#Getting all needed packages and credentials

import datetime
import tweepy
import pandas as pd
import time
import pip
import random
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



all_tweets = pd.read_csv('twitter_list.csv')
twitter_list_used = pd.read_csv('twitter_list_used.csv')

all_tweets['created'] = pd.to_datetime(all_tweets['created'])
all_tweets.sort_values(by='created', ascending=False)

tweeters_to_tweet = all_tweets[~all_tweets.name.isin(twitter_list_used.name)]
tweeters_to_tweet.sort_values(by='created', ascending=False)
this_runs_tweets = tweeters_to_tweet.head(5)

frames = [this_runs_tweets, twitter_list_used]
tweets_to_exclude = pd.concat(frames)
tweets_to_exclude.to_csv(r'twitter_list_used.csv', index = False)


##let's get our responses ready here 
responses = [
    
             "I don\'t miss my baby not sleeping! If it\'s useful at all this book helped us so much!     https://uk.bookshop.org/a/4752/9781849536851",
             "I remember when we didn\'t sleep more than an hour at a time! We ended up using The Baby Sleep Guide and I can\'t recommend it enough'!     https://uk.bookshop.org/a/4752/9781849536851",
             "If it\'s of any use we use the baby sleep guide to help our little one sleep for longer and it's been a real help!     https://uk.bookshop.org/a/4752/9781849536851",
             "It might help to use a book like the one we used (if you\'re baby isn't giving you much rest!     https://uk.bookshop.org/a/4752/9781849536851",
             "https://uk.bookshop.org/a/4752/9781849536851     This book was a really help for us and our baby",
             "Have you tried this book? Its a sleep training we used and it helped us out a lot!     https://uk.bookshop.org/a/4752/9781849536851",
             "We used this and it might help!     https://uk.bookshop.org/a/4752/9781849536851",
             "I feel for anyone not sleeping because of a newborn, we used this book which might help someone!     https://uk.bookshop.org/a/4752/9781849536851",
             "This baby sleep guide was a welcome read in our home!     https://uk.bookshop.org/a/4752/9781849536851",
             "Linking a book that we used to help out little one sleep better!     https://uk.bookshop.org/a/4752/9781849536851",
             "We used The Baby Sleep Guide and I can\'t recommend it enough'!     https://uk.bookshop.org/a/4752/9781849536851",            
             "I\'ve linked the book that we used to help our little one sleep better!     https://uk.bookshop.org/a/4752/9781849536851",
             "If it\'s all all useful we use the baby sleep guide to help our baby sleep for longer and it's been really great!     https://uk.bookshop.org/a/4752/9781849536851",
             "It might help to use a book like this one we used (if you\'re baby isn't sleeping for long!     https://uk.bookshop.org/a/4752/9781849536851",
             "I don\'t miss our baby not sleeping! If it\'s useful at all this book helped us so much!     https://uk.bookshop.org/a/4752/9781849536851",
             "I remember when we didn\'t sleep more than an hour at a time! We ended up reading The Baby Sleep Guide and I can\'t recommend it enough'!     https://uk.bookshop.org/a/4752/9781849536851",
             "If it\'s of any use we used the baby sleep guide to help our baby sleep for longer periods and truly recommend it!     https://uk.bookshop.org/a/4752/9781849536851",
             "Have you tried the baby sleep guide book? Its a sleep training we used and it helped us out a lot!     https://uk.bookshop.org/a/4752/9781849536851",
             "It\'s so hard getting no sleep, we used this book which might help someone!     https://uk.bookshop.org/a/4752/9781849536851",
             "Linking a book that we used when we got no sleep from our little one!     https://uk.bookshop.org/a/4752/9781849536851"

            ]

mult_responses = responses*10
mult_responses = pd.DataFrame(mult_responses)
mult_responses.columns = ['response']
mult_responses = mult_responses.sample(frac=1)


## let's tweet!

response_point = 0

for index, row in this_runs_tweets.iterrows():
    sleep(randint(10,50))
    tweet_id = (row['tweet_id'])
    naming = (row['name'])
    x = '@'
    print(naming)
    y = mult_responses['response'].iloc[response_point]
    response_point +=1
    reply_status = " %s%s %s" % (x,naming,y)
    api.update_status(reply_status, tweet_id, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    
quit()

