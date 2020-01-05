import pandas as pd
import numpy as np
import csv
from os import listdir
from os.path import isfile, join


mypath = "../../Tweets/"  # dove si trovano i tweet di ogni utente
# path dove salvare i file excel contenenti i tweet puliti
path_to_write = "../dist/clean_users/"

# ottengo una lista dei nomi di tutti i file presenti nella cartella specificata
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# FILTRI
# Data di partenza
starting_date = "2019-01-01 00:00:00"  # inizio 2019
ending_date = "2019-12-31 23:59:59"  # fine 2019
# Minimo numero di Tweet totali accettati
tweet_input_threshold = 100
# Parole chiave da ricercare
keywords = ("salvini", "di maio", "renzi", "berlusconi")
# Minimo numero di Tweet "politici" accettati
tweet_filtered_threshold = 50


def hasKeywords(text):  # funzione per la ricerca di parole chiave
    for k in keywords:
        if k in text:
            return True
    return False


def filterTweet(tweet):
    return tweet["created_at"] > starting_date and tweet["created_at"] < ending_date and hasKeywords(tweet["full_text"])


def filterUserTweets(tweets):
    return len(tweets) > tweet_filtered_threshold


def insertTweets(tweets, filename):  # funzione per inserire un tweet nel database
    with open(path_to_write+filename, mode="w", encoding="utf8") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerows(tweets)


for i in range(len(files)):  # per ogni file
    file_name = files[i]
    data = pd.read_csv(mypath+file_name, sep=",",
                       encoding="utf8")
    df = pd.DataFrame(data)
    tweets = []
    for i in range(1, len(df)):
        tweet = df.iloc[i]  # per ogni tweet dell'utente
        if filterTweet(tweet):  # filtro secondo le regole definite
            tweets.append(tweet)
    # ho completato la lista dei tweet per questo utente: lancio la scrittura su csv della lista
    if filterUserTweets(tweets):  # filtro sul numero di tweet filtrati
        # taglio e prendo solo i primi 50 tweet
        insertTweets(tweets[:50], file_name)

print("Done with 0 errors")
