import pandas as pd
import numpy as np
import csv
from os import listdir
from os.path import isfile, join


mypath = "../../Tweets/"  # dove si trovano i tweet di ogni utente
# ottengo una lista dei nomi di tutti i file presenti nella cartella specificata
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# filtro sui tweet in ingresso
starting_date = "2019-01-01 00:00:00"  # inizio 2019
# filtro sul numero di tweet dell'utente in input
tweet_input_threshold = 100
# filtro sul numero di tweet dell'utente dopo il filtro
tweet_filtered_threshold = 50
# lista di parole chiave da cercare
keywords = ("salvini", "di maio")
# path dove salvare i file excel
path_to_write = "../dist/clean_users/"


def hasKeywords(text):
    for k in keywords:
        if k in text:
            return True
    return False


def insertTweets(tweets, filename):  # funzione per inserire un tweet nel database
    with open(path_to_write+filename, mode="w", encoding="utf8") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerows(tweets)


for i in range(len(files)):  # per ogni file
    file = files[i]
    data = pd.read_csv(mypath+file, sep=",",
                       encoding="utf8")  # leggo con pandas
    df = pd.DataFrame(data)  # estraggo il dataframe
    if len(df) >= tweet_input_threshold:  # filtro sul numero iniziale dei tweet
        tweets = []  # variabile per contenere i tweet formattati correttamente per l'inserimento nel db
        for i in range(1, len(df)):  # per ogni tweet dell'utente
            # filtro sulla data di creazione
            if df.iloc[i]["created_at"] > starting_date and hasKeywords(df.iloc[i]["full_text"]):
                tweets.append((str(df.iloc[i]["id"]), str(df.iloc[i]["created_at"]), str(df.iloc[i]["favorites"]), str(
                    df.iloc[i]["retweets"]), str(df.iloc[i]["source"]), str(df.iloc[i]["full_text"])))  # aggiungo il tweet alla lista da salvare su db
            pass
        # ho completato la lista dei tweet per questo utente: lancio la scrittura su csv della lista
        if len(tweets) > tweet_filtered_threshold:
            insertTweets(tweets[:50], file)
    pass

print("Done with 0 errors")
