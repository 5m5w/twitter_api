import tweepy
import textwrap
import config
from tweepy.auth import OAuthHandler

client = tweepy.Client(config.Bearer_Token,config.API_KEY,config.API_KEY_SECRET, config.Access_Token, config.Access_Token_Select)

auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.Access_Token, config.Access_Token_Select)
api = tweepy.API(auth)

#make a tweet
response = client.create_tweet(text="test from tweepy")
print(response)

# public_tweets = api.home_timeline()
# print(public_tweets)
# try:
#     api.verify_credentials()
#     print('yes')
# except:
#     print('failed')
