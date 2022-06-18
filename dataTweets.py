"""
Roberta Model for NLP, to clasiffy tweets into neutral, positive and negative. This model was develop by META AI.

"""
## // Libraries //

import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import os 
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from scipy.special import softmax
## // Consumer keys //

consumer_key = "POCoAXRSQiMqau0a53VohlAX8"
consumer_secret = "8vxBOC7gC5MsEGfZjCXdFcFxnqmqarsT1vjUK3l72n2YAkxsr1"
access_token = "1528920668603023361-OMORmijptU4lT0sN45VMxOt5hhhzS0"
access_token_secret = "re77B607BQ8IJASicUNRMWlrA8to1v4wPxs9jUkX0Btwf"
bearer_token = "AAAAAAAAAAAAAAAAAAAAADu0cwEAAAAA97s1XjvpF90B7yGZvNCNDvL5M9U%3DTsEvlFpF0m6U3NQlDz7tXHCFgqZLwVbD0CIgxFIOBUgQGEqXtu"

## // Create authentication object //
authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)

## //Set the access token //
authenticate.set_access_token(access_token, access_token_secret)

# //Create the API object //
api = tweepy.API(authenticate, wait_on_rate_limit = True)

search_term = "#bitcoin -filter:retweets"
limit = 100
tweets = tweepy.Cursor(api.search_tweets, q = search_term, count= 100, since_id="2022-01-01", lang = "en", tweet_mode = "extended" ).items(limit)

all_tweets = [tweet.full_text for tweet in tweets]

## // Create a dataframe to store the tweets //
df = pd.DataFrame(all_tweets, columns = ["Tweets"])
df

# // Cleaning the tweets for the Roberta model//
cleand_tweets = []
for twt in all_tweets:
    twt = re.sub("#bitcoin", "bitcoin",twt)
    twt = re.sub("#Bitcoin", "Bitcoin",twt)
    twt = re.sub("#[A-Za-z0-9]+", "",twt)
    twt = re.sub("\\n","",twt)
    twt = re.sub("@[A-Za-z0-9]+", "@user",twt)
    twt = re.sub("https?:\/\/\S+","http",twt)
    cleand_tweets.append(twt)



print(cleand_tweets)