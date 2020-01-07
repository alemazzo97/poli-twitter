import pandas as pd
import numpy as np

path = "../data/labelled/"
file_name = "without_unknown"
data = pd.read_csv(path+file_name+".csv", sep=",", encoding="utf8")
df = pd.DataFrame(data)

lefties = 0
righties = 0
tot = len(df)

training_set = []
test_set = []

lefties = []
righties = []
for i in range(10):
    user = [df.iloc[i]["twitter_id"],df.iloc[i]["sex"],df.iloc[i]["partito"]]
    if df.iloc[i]["partito"] == -1:
        lefties.append(user)
    else:
        righties.append(user)

