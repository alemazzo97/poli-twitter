import os
import pandas as pd
import datetime 
from langdetect import detect
import re
import shutil

def remove_newlines(string):
    return re.sub(u'[\n]', ' ', string)

def remove_url(string):
    return " ".join([ el for el in remove_newlines(string).split(" ") if not (el.lower() == ("rt") or el.lower().startswith("http"))])# or el.lower().startswith("@"))])
    
def remove_special(string):
    return re.sub(u'[^A-Za-z0-9\sàèìòùáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ.,?!\"$%&(){}[\]=:;-@*\+#\']', '', remove_url(string))

def get_hashtags(string):
    return [el for el in remove_newlines(string).split(" ") if re.sub('\s', '', el).startswith('#')]


path = "D://CBSD/Tweets"

starting_date =  datetime.datetime(2018,12,31)
def remove_dir():
    try:
        if not os.path.exists(path + "/cleaned_tweets"):
            os.makedirs(path + "/cleaned_tweets")
        else:
            shutil.rmtree(path + "/cleaned_tweets")
            os.makedirs(path + "/cleaned_tweets")
    except:
        remove_dir()

remove_dir()

def clean_tweets(el):
    i = 0
    try:
        df = pd.read_csv(path + "/" + el,encoding='utf-8-sig')
        if len(df) > 50:
            res = []
            for tweet in range(len(df)):
                cleaned_tweets = remove_special(df.iloc[tweet]["full_text"])
                if datetime.datetime.strptime(df.iloc[tweet]["created_at"], '%Y-%m-%d %H:%M:%S') > starting_date and len(cleaned_tweets) > 10:
                    res.append([cleaned_tweets])
            if len(res) > 50:
                pd.DataFrame(res).to_csv(path + "/cleaned_tweets/" + el.split(".")[0] + ".csv", sep="," ,encoding='utf-8-sig', header=["text"])
    except:
        i += 1
for el in os.listdir(path):
    clean_tweets(el)