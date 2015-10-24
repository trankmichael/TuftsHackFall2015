import indicoio
import pandas as pd
import csv

step_size = 200
indicoio.config.api_key = 'cefae61c6968c29ea880d918e9a6095d'
key2 = 'bff000095c5eb591fa1b4ab3da98063b'

df = pd.read_csv('data/hotel_reviews.csv')
reviews = df['text'].tolist()
sentiment = []
steps = len(sentiment) / step_size
leftover = len(sentiment) % step_size
total_count = 0
for i in xrange(steps):
    total_count += step_size
    if total_count > 20000:
        indicoio.config.api_key = 'bff000095c5eb591fa1b4ab3da98063b'
    test = reviews[i * step_size:(i + 1) * step_size]
    sentiment.extend(indicoio.batch_sentiment(test))
test = reviews[total_count:]
sentiment.extend(indicoio.batch_sentiment(test))
csv_sent = [[x] for x in sentiment]
resultFile = open("sentiment_results.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(csv_sent)