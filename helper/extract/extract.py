# extract data
import GetOldTweets3 as got
import datetime
import numpy as np
import pandas as pd
from tqdm import tqdm
import time

def get_data(start_date,end_date,month):

  for i in tqdm(range(start_date, end_date)):
    dt = datetime.datetime(2020,month,i)
    dt_end = dt + datetime.timedelta(days=1)
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona OR covid19 OR covid OR lockdown OR coronavirus')\
                                            .setSince(dt.strftime("%Y-%m-%d"))\
                                            .setUntil(dt_end.strftime("%Y-%m-%d"))\
                                            .setLang('en')\
                                            .setMaxTweets(5000)\
                                            .setWithin("1000km")\
                                            .setNear("Bhopal,India")
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tw.username,
                  tw.text,
                  tw.date,
                  tw.retweets,
                  tw.favorites,
                  tw.mentions,
                  tw.hashtags] for tw in tweet]
      
    news_df = pd.DataFrame(text_tweets, 
                              columns = ['user', 'text','date','favorites', 'retweets', 'mentions', 'hashtags'])
    news_df.to_csv(dt.strftime("%Y-%m-%d") + '.csv', index=False)
    time.sleep(10)
  return "Success";  

get_data(1,2,4)  
