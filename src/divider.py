import pandas as pd
import numpy as np

data = pd.read_csv("../data/LabelledAccounts.csv", sep=";", encoding="utf8")
df = pd.DataFrame(data)

lista = ["SID 1", "SID 2", "SID 3", "SID 4", "SID 5"]
for i in range(len(df)):
    # per ogni utente estraggo i voti che gli sono stati dati
    # sommo tutti i punteggi per la destra e tutti quella per la sinistra
    # se tende più a sinistra o a destra e categorizzo di conseguenza
    sx = 0
    dx = 0
    for sid in lista:
        if df.iloc[i][sid] == 1:
            sx += 1
        elif df.iloc[i][sid] == 2:
            dx += 1

    if dx == 0 and sx == 0:
        print("BOH")
    elif dx > sx:
        print("Destra")
    else:
        print("Sinistra")
