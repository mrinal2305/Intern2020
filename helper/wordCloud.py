import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
from tqdm import tqdm
import datetime

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceKey.json"

def plot_wordcloud(text, mask=None, max_words=200, max_font_size=100, figure_size=(24.0, 16.0), color='white',
                   title=None, title_size=40, image_color=False):
    stopwords = set(STOPWORDS)
    more_stopwords = {'u', "im","thi","ji","us","ha","um","hi","be","will","by","is","of","to"}
    stopwords = stopwords.union(more_stopwords)

    wordcloud = WordCloud(background_color=color,
                          stopwords=stopwords,
                          max_words=max_words,
                          max_font_size=max_font_size,
                          random_state=42,
                          width=200,
                          height=200,
                          mask=mask,
                          colormap=matplotlib.cm.inferno)
    wordcloud.generate(text)

    plt.figure(figsize=figure_size)
    if image_color:
        image_colors = ImageColorGenerator(mask)
        plt.imshow(wordcloud.recolor(color_func=image_colors),
                   interpolation="bilinear")
        plt.title(title, fontdict={'size': title_size,
                                   'verticalalignment': 'bottom'})
    else:
        plt.imshow(wordcloud)
        plt.title(title, fontdict={'size': title_size, 'color': 'black',
                                   'verticalalignment': 'bottom'})
    plt.axis('off')
    plt.tight_layout()
    return wordcloud


def getOuptput(folder, month, str_date, end_date):
    for i in tqdm(range(str_date, end_date)):
        dt = datetime.datetime(2020, month, i).strftime("%Y-%m-%d")
        location = "gs://tourist-bot-hilapp.appspot.com/" + \
            folder+"/"+str(dt)+'.csv'
        df = pd.read_csv(location)
        df = df[['clean_text']]
        allWords=''.join([tweet for tweet in df['clean_text']])
        pos_mask = np.array(Image.open('twitter_mask.png'))
        twitterwordcloud=plot_wordcloud(allWords,mask=pos_mask,color='white',max_font_size=100,title_size=30,title="WordCloud of Tweets")
        twitterwordcloud.to_file('wordCloud/'+dt+'.png')

# getOuptput("March_clean",3,23,32)
# getOuptput("April_clear",4,11,31)
# getOuptput("May_clear",5,1,32)
# getOuptput("June_clear",6,1,28)
# Run
getOuptput("April_clear",4,1,11)