# Questo script prende in input gli utenti classificati con "labeler.py"
# e si occupa di suddividerli in due set:
# - training set
# - test set
# Per creare questi set in modo che abbiano lo stesso rapporto di utenti di destra e sinistra
# ho creato due liste separate di utenti solo di destra e di utenti solo di sinistra
# poi le ho spezzate a partire da una percentuale fissata della loro dimensione
# creando i due set finali di training e test

import pandas as pd
import numpy as np

path = "../data/labelled/"
file_name = "without_unknown"
data = pd.read_csv(path+file_name+".csv", sep=",", encoding="utf8")
df = pd.DataFrame(data)

lefties = 0
righties = 0
tot = len(df)
print("Total users: "+str(tot))

lefties = []
righties = []
for i in range(tot):
    user = [df.iloc[i]["twitter_id"], df.iloc[i]["sex"], df.iloc[i]["partito"]]
    if df.iloc[i]["partito"] == -1:
        lefties.append(user)
    else:
        righties.append(user)

print("Left users: " + str(len(lefties)))
print("Right users: " + str(len(righties)))

# definisco la percentuale che voglio
training_percentage = 0.8
test_percentage = 1-training_percentage

# ottengo il valore approssimato percentuale (x%) tra destra e sinistra
trainingL = round(len(lefties)*training_percentage)
trainingR = round(len(righties)*training_percentage)

# estraggo i primi x% da entrami i set e li unisco per formare il training set
training_set = lefties[:trainingL] + righties[:trainingR]
# estraggo gli utlimi (1-x)% da entrami i set e li unisco per formare il test set
test_set = lefties[trainingL:] + righties[trainingR:]

print("Training set: "+str(len(training_set)) +
      " => " + str(round(len(training_set)/tot*100))+"%")
print("Test set: " + str(len(test_set))+" => " +
      str(round(len(test_set)/tot*100))+"%")

# salvo i due set
path_to_save = "../data/set/"
pd.DataFrame(training_set).to_csv(path_to_save+"training.csv", sep=",",
                                  encoding='utf-8-sig', header=["twitter_id", "sex", "partito"])
print("training.csv saved")
pd.DataFrame(test_set).to_csv(path_to_save+"test.csv", sep=",",
                              encoding='utf-8-sig', header=["twitter_id", "sex", "partito"])
print("test.csv saved")
