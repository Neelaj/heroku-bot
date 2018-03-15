# Dependencies
import tweepy
import json
import time

#dkfsad
#add some new rows forupdate check 
# Twitter API Keys
consumer_key = "qevrTKrs9tGBJgH5w9aBExdCr"
consumer_secret = "TgaCQHOmONZQlbyDfvC5wcuq4FqQ6HxCZVPy9ViBbgzsRjHYyr"
access_token = "969400800119177216-z7VgIssjy0JYdSLDwV7ez85sTe4J2OS"
access_token_secret = "suQgqFOPBfFtAgE692ARb0HPumEfMNZzJldhQaoQV8uXK"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE