import pandas as pd
import numpy as np

path = "../data/labelled/"
file_name = "without_unknown"
data = pd.read_csv(path+file_name+".csv", sep=",", encoding="utf8")
df = pd.DataFrame(data)

lefties = 0
righties = 0
males = 0
females = 0
tot = len(df)
for i in range(tot):
    partito = df.iloc[i]["partito"]
    if partito == -1:
        lefties += 1
    elif partito == 1:
        righties += 1
    sex = df.iloc[i]["sex"]
    if sex == "M":
        males += 1
    elif sex == "F":
        females += 1

p_L = round(lefties/tot*100)
p_R = round(righties/tot*100)
p_U = round((tot-lefties-righties)/tot*100)

print("L: "+str(p_L)+"%")
print("R: "+str(p_R)+"%")
print("U: "+str(p_U)+"%")

p_M = round(males/tot*100)
p_F = round(females/tot*100)
p_U = round((tot-males-females)/tot*100)

print("M: "+str(p_M)+"%")
print("F: "+str(p_F)+"%")
print("U: "+str(p_U)+"%")
