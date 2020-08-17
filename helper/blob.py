import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import pandas as pd
import os
from tqdm import tqdm
import datetime

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceKey.json"

date    = []
subject = []
polar   = []

def getScore(text):
    sub = TextBlob(text).sentiment.subjectivity
    polar = TextBlob(text).sentiment.polarity

# def getPolarity(text):
#     return TextBlob(text).sentiment.polarity

# def getSubjectivityFile(location):
#     try:
#         loc = location
#         df = pd.read_csv(loc)
#         df = df[['clean_text']]
#         df['Subjectivity'] = df["clean_text"].apply(getSubjectivity)
#         df['Polarity'] = df["clean_text"].apply(getPolarity)
#         avg_polarity = df['Polarity'].mean()
#         avg_subjectivtiy = df['Subjectivity'].mean()
#         arr = [avg_polarity, avg_subjectivtiy]
#         subject.append(avg_subjectivtiy)
#         polar.append(avg_polarity)
#         return arr
#     except Exception as e:
#         return e

# def getOuptput(folder,month,str_date,end_date):   
#  for i in tqdm(range(str_date, end_date)):
#    dt = datetime.datetime(2020,month,i).strftime("%Y-%m-%d")
#    location = "gs://tourist-bot-hilapp.appspot.com/"+folder+"/"+str(dt)+'.csv'
#    date.append(dt)
#    getSubjectivityFile(location)

# getOuptput("March_clean",3,23,32)
# getOuptput("April_clear",4,1,31)
# getOuptput("May_clear",5,1,32)
# getOuptput("June_clear",6,1,28)

# # storing final output in csv
# df = pd.DataFrame()
# df['date'] = date
# df['subjectivity'] = subject
# df['polarity'] = polar

# df.to_csv("output.csv",index=False)