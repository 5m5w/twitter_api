import tweepy
import textwrap
import config
from tweepy.auth import OAuthHandler
from time import sleep

client = tweepy.Client(config.Bearer_Token,config.API_KEY,config.API_KEY_SECRET, config.Access_Token, config.Access_Token_Select)

auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.Access_Token, config.Access_Token_Select)
api = tweepy.API(auth)

long_text = r"M11 Credit於周三在基於區塊鏈的信貸市場Maple Finance上重新開放貸款，並為其新的加密貸款池籌集新資金，該公司在推特上表示。它還任命了一位新的信貸負責人，並升級了其風險管理和信貸審核程序，Maple博客文章稱。此前，M11 Credit管理的池子遭受3600萬美元的违約，其他貸款未能償還，並在11月份加密交易所FTX崩潰後重組。雖然一些加密觀察家將FTX的突然崩潰視為黑天鵝事件，但隨後對交易公司和貸款人的擴散強調了加密貸款在風險管理和信貸審核方面的缺陷。值得注意的是，M11池子的最大借款人之一Orthogonal Trading涉嫌通過歪曲其財務和FTX損失來誤導M11和Maple。因此，受影響池子的投資者對其存款面臨高達80％的損失。在此事件之後"

chunks = [long_text[i:i+150] for i in range(0, len(long_text), 150)]
tweet1 = api.update_status(chunks[0])
previous_tweet_id = tweet1.id
for text in chunks[1:]:
    tweet = api.update_status(text, in_reply_to_status_id=previous_tweet_id)
    previous_tweet_id = tweet.id

# 將每個tweet在後面加上頁數
# for i, chunk in enumerate(chunks):
#     tweet1 = api.update_status(f'{chunk}({i+1}/{len(chunks)})')
#     print(tweet1)

# try:
#     api.verify_credentials()
#     print('yes')
# except:
#     print('failed')
