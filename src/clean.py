import os
import pandas as pd
import datetime 
from langdetect import detect
import re
import shutil

# parole chiave da cercare all'interno dei tweets

keys = [
    "immigrat",
    "figli",
    "votar",
    "destra",
    "elezion",
    "famigli",
    "parlament",
    "stelle",
    "movimento",
    "matteo",
    "capitan",
    "vot",
    "partit",
    "sinistr",
    "maio",
    "sold",
    "politic",
    "president",
    "lavor",
    "paes",
    "ministr",
    "ue",
    "grillo",
    "ilva",
    "salvinirispondi",
    "segre",
    "movimento5stelle",
    "pd",
    "conte",
    "dimaio",
    "renzi",
    "sardin",
    "bibbiano",
    "stopmes",
    "mes",
    "meloni",
    "italia",
    "raggi",
    "govern",
    "redditodicittadinanza",
    "crisidigoverno",
    "migrant",
    "berlusconi",
    "mattarella",
    "openeuro",
    "italiaviva",
    "leg",
    "salvini",
    "m5s",
    "matteosalvinimi",
    "mov5stelle",
    "giorgiameloni",
    "luigidimaio",
    "matteorenzi",
    "virginiaraggi",
    "giuseppeconteit",
    "repubblic",
    "pdnetwork",
    "legasalvini",
    "beppegrillo",
    "fratelliditaiia",
    "lauraboldrini",
    "forzaitalia",
    "liberoofficial",
    "noiconsalvini",
    "salvinimi",
    "paologentiloni",
    "m5ssenato"
]

# path contiene l'indirizzo della cartella con i tweets, al cui interno successivamente crea la cartella cleaneed_tweets 
# con la prima pulizia e al cui interno crea la cartella only_with_keys che contiene solo gli utenti che hanno almeno minimum_tweets tweet
# contenenti le parole chiave scelte contenute nella variabili keys

path = "D://CBSD/Tweets"

# starting_date contiene la data oltre la quale vengono tenuti i tweets

starting_date =  datetime.datetime(2018,12,31)

# scarta se ci sono meno di minimum_tweets tweets dopo ogni pulizia

minimum_tweets = 50

def remove_newlines(string):
    return re.sub(u'[\n]', ' ', string)

def remove_url(string):
    return " ".join([ el for el in remove_newlines(string).split(" ") if not (el.lower() == ("rt") or el.lower().startswith("http"))])# or el.lower().startswith("@"))])
    
def remove_special(string):
    return re.sub(u'[^A-Za-z0-9\sàèìòùáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ.,?!\"$%&(){}[\]=:;-@*\+#\']', '', remove_url(string))

def get_hashtags(string):
    return [el for el in remove_newlines(string).split(" ") if re.sub('\s', '', el).startswith('#')]

# rimuove la cartella name in path se resente e la ricrea

def remove_dir(name):
    try:
        if not os.path.exists(path + name):
            os.makedirs(path + name)
        else:
            shutil.rmtree(path + name)
            os.makedirs(path + name)
    except:
        remove_dir()


remove_dir(name="/cleaned_tweets")

# rimuove caratteri speciali(link, emoticon, ...) dai tweet e cancella non tiene i tweet prima di starting_date, inoltre tiene solo gli utenti con almeno
# minimum_tweets tweets

def clean_tweets():
    for el in os.listdir(path):
        try:
            df = pd.read_csv(path + "/" + el,encoding='utf-8-sig')
            if len(df) > minimum_tweets:
                res = []
                for tweet in range(len(df)):
                    cleaned_tweets = remove_special(df.iloc[tweet]["full_text"])
                    if datetime.datetime.strptime(df.iloc[tweet]["created_at"], '%Y-%m-%d %H:%M:%S') > starting_date and len(cleaned_tweets) > 10:
                        res.append([cleaned_tweets])
                if len(res) > minimum_tweets:
                    pd.DataFrame(res).to_csv(path + "/cleaned_tweets/" + el.split(".")[0] + ".csv", sep="," ,encoding='utf-8-sig', header=["text"])
        except:
            print("err")

clean_tweets(el) # ------------------ CI METTE ORE ------------------- se già fatto commentare questa riga, sennò cancella e riparte

# serviva per vedere quali fossero parole, hashtag e @ più comuni
'''
res = {}
for el in os.listdir(path):
    try:
        df = pd.read_csv(path + "/cleaned_tweets/" + el,encoding='utf-8-sig')
        for phrase in df["text"]:
            p = re.sub(u'[,:]', ' ', phrase)
            p = re.sub("  ", ' ', p)
            for word in p.split(" "):
                word = word.lower()
                if word in res:
                    res[word] += 1
                else:
                    res[word] = 1
        print(i)
        i += 1
    except:
        print("err")
print(res)

from stop_words import get_stop_words
stop_words = get_stop_words('it')

dictlist = []
for key, value in res.items():
    temp = [key,value]
    dictlist.append(temp)
    
def myFunc(a):
    return a[1]

dictlist.sort(reverse=True, key=myFunc)
dictlist
'''

# crea la cartella /cleaned_tweets/only_with_keys e dentro salva solo gli utenti che hanno almeno minimum_tweets tweets con parole chiave 

remove_dir(name="/cleaned_tweets/only_with_keys") # crea la cartella /cleaned_tweets/only_with_keys

def remove_no_keys():
    for el in os.listdir(path + "/cleaned_tweets"):
        try:
            print(el)
            df = pd.read_csv(path + "/cleaned_tweets/" + el, encoding='utf-8-sig')
            res = []
            for phrase in df["text"]:
                for keyword in keys:
                    if keyword in phrase:
                        res.append(phrase)
                        break
            if len(res) > minimum_tweets:
                pd.DataFrame(res).to_csv(path + "/cleaned_tweets/only_with_keys/" + el, sep="," ,encoding='utf-8-sig', header=["text"])
        except:
            print("err")

remove_no_keys()