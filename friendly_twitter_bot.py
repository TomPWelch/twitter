
#downloading all the needed packages

import datetime
import tweepy
import pandas
import time
import pip


#adding all the keys/secrets etc for my app in twitter

consumer_key = 'XXXXX' 
consumer_secret = 'XXXXX' 
access_token = 'XXXX-XXXX' 
access_token_secret = 'XXXX' 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#looking at all London based, Desktop (because they're more likely to be able to open google docs) queries which reference Asda
d = pandas.DataFrame()

for tweets in tweepy.Cursor(api.search,
                        q="Asda",
                        rpp=100,
                        geocode="51.5074,0.1278,33km",
                        result_type="recent",
                        source = "Twitter For Web",
                        include_entities=True,
                        lang="en").items(1000):
    
                        temp = pandas.DataFrame(
                        {
                            'text': tweets.text,
                            'name': tweets.user.screen_name,
                            'created': tweets.created_at,
                            'tweet_id': tweets.id
                        },
                            index=[0]                 
    )
                        d = pandas.concat([d, temp])


print(d)

#looking at all London based, Desktop (because they're more likely to be able to open google docs) queries which reference Ocado
e = pandas.DataFrame()

for tweets in tweepy.Cursor(api.search,
                        q="Ocado",
                        rpp=100,
                        geocode="51.5074,0.1278,33km",
                        result_type="recent",
                        include_entities=True,
                        source = "Twitter For Web",
                        lang="en").items(1000):
    
                        temp = pandas.DataFrame(
                        {
                            'text': tweets.text,
                            'name': tweets.user.screen_name,
                            'created': tweets.created_at,
                            'tweet_id': tweets.id
                        },
                            index=[0]                 
    )
                        e = pandas.concat([e, temp])

print(e)

#putting these queries in one dataframe

frames = [d, e]
result = pandas.concat(frames)

#removing duplicates so I don't spam anyone
names_df = result[['name', 'tweet_id']]
names_df_dedup = names_df.drop_duplicates("name", keep='first')

#lets also not message the shops directly!
names_df_dedup = names_df_dedup[names_df_dedup.name != 'Ocado']
names_df_dedup = names_df_dedup[names_df_dedup.name != 'Asda']

#We need to create a file of everyone we've tweeted in the past, so run this code the first time only
#names_df_dedup.to_csv(r'twitter_list.csv', index = False)

#get the list of everyone we've tweeted aleady tweeted in previous runs
twitter_list = pandas.read_csv('twitter_list.csv')
tweeters_to_message = names_df_dedup 
tweeters_to_exclude = twitter_list.name

#Now lets see who we've got in today's list that we can't tweet because we've already tweeted them
message_list_and_exclusions = tweeters_to_message.merge(tweeters_to_exclude.drop_duplicates(), on=['name','name'], how='left', indicator=True)
tweeters_to_tweet = message_list_and_exclusions[message_list_and_exclusions['_merge'] == 'left_only']

#Now put the whole list of handles into the twitter_list.csv file (i.e. lets add in the people we're not going to tweet again)
message_list_and_exclusions.to_csv(r'twitter_list.csv', index = False)
#print(tweeters_to_tweet)

#Now let's start tweeting these people (in reply to their tweets!)

for index, row in tweeters_to_tweet.iterrows():
    time.sleep(122)
    tweet_id = (row['tweet_id'])
    naming = (row['name'])
    x = '@'
    print(tweet_id)
    print(naming)
    print(x)
    y = 'There are a bunch of small businesses still delivering fresh food in London, theres a list of 158 of them here! https://docs.google.com/spreadsheets/d/165w7-Gj2CEoXhhzZ2RMbky45DlvQyX-oE0sXjkgWNEY/edit#gid=0'
    reply_status = " %s%s %s" % (x,naming,y)
    api.update_status(reply_status, tweet_id)





