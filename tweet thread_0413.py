import tweepy
import config
from tweepy.auth import OAuthHandler
from time import sleep

client = tweepy.Client(config.Bearer_Token,config.API_KEY,config.API_KEY_SECRET, config.Access_Token, config.Access_Token_Select)

auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.Access_Token, config.Access_Token_Select)
api = tweepy.API(auth)

long_text = r""

chunks = [long_text[i:i+140] for i in range(0, len(long_text), 140)]
tweet1 = api.update_status(chunks[0])
previous_tweet_id = tweet1.id
for text in chunks[1:]:
    tweet = api.update_status(text, in_reply_to_status_id=previous_tweet_id)
    previous_tweet_id = tweet.id
    sleep(3)
# 將每個tweet在後面加上頁數
# for i, chunk in enumerate(chunks):
#     tweet1 = api.update_status(f'{chunk}({i+1}/{len(chunks)})')
#     print(tweet1)

# try:
#     api.verify_credentials()
#     print('yes')
# except:
#     print('failed')
