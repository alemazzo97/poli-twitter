import pandas as pd
from textblob import TextBlob
from googletrans import Translator
translator = Translator()

# frase = "Grazie sindaco! Quando prevede interventi in viale Corsica e strade limitrofe? Venga a dare una occhiata, credo sia importante."
data = pd.read_csv("../dist/clean_users/100_lyon_tweets.csv", sep=",", encoding="utf8")
df = pd.DataFrame(data)
print(df)


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


# def removeLink(word):
#     if word.starts_with("http")
#     return ""
#     else return word


sum_of_polarities = 0

for i in range(0, 50):
    tweet_ita = df.iloc[i][5]
    print(tweet_ita)
    tweet_ita = deEmojify(tweet_ita)
    tweet = translator.translate(tweet_ita, dest='en').text
    print(tweet)
    sum_of_polarities += TextBlob(tweet).sentiment.polarity

print(sum_of_polarities/len(df))
