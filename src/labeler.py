import pandas as pd
import numpy as np
import math

data = pd.read_csv("../data/LabelledAccounts.csv", sep=";", encoding="utf8")
df = pd.DataFrame(data)

lista = ["SID 1", "SID 2", "SID 3", "SID 4", "SID 5"]
users = []
for i in range(len(df)):
    # per ogni utente estraggo i voti che gli sono stati dati
    # sommo tutti i punteggi per la destra e tutti quella per la sinistra
    # se tende più a sinistra o a destra e categorizzo di conseguenza
    sx = 0
    dx = 0
    for sid in lista:
        try:
            voto = float(df.iloc[i][sid])
            pass
        except:
            voto = 0
            pass
        if not math.isnan(voto):

            if voto == 2:  # pd = sinistra
                sx += 1
            elif voto != 4:  # diverso da m5s (non classificato)
                dx += 1

    partito = 0
    if dx != 0 or sx != 0:  # almeno uno diverso da zero
        if dx > sx:  # se vince in modo stretto la desta
            partito = 1
        else:  # altrimenti sinistra
            partito = -1

    # print(df.iloc[i]["Twitter ID"]+": "+partito)
    if partito != 0:
        new_user = [df.iloc[i]["Twitter ID"], df.iloc[i]["Sex"], partito]
        users.append(new_user)

# print(users)
path_to_save = "../data/labelled/"
pd.DataFrame(users).to_csv(path_to_save+"without_unknown.csv", sep=",",
                           encoding='utf-8-sig', header=["twitter_id", "sex", "partito"])
