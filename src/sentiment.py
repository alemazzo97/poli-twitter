import pandas as pd
from textblob import TextBlob
from googletrans import Translator
translator = Translator()

# frase = "Grazie sindaco! Quando prevede interventi in viale Corsica e strade limitrofe? Venga a dare una occhiata, credo sia importante."
your_path = "../dist/clean_users/"
your_file = "100_lyon_tweets.csv"
data = pd.read_csv(your_path+your_file, sep=",", encoding="utf8")
df = pd.DataFrame(data)
print(df)


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


sum_of_polarities = 0
how_many_users = 50
for i in range(0, how_many_users):
    tweet_ita = df.iloc[i][5]  # posizione del full_text
    # print(tweet_ita)
    tweet_ita = deEmojify(tweet_ita)
    tweet = translator.translate(tweet_ita, dest='en').text
    # print(tweet)
    sum_of_polarities += TextBlob(tweet).sentiment.polarity

print(sum_of_polarities/len(df))
