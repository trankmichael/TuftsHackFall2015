import pandas as pd
import indicoio
import csv
indicoio.config.api_key = 'cefae61c6968c29ea880d918e9a6095d'


def clean_for_tableau(csv_file):
    df = pd.read_csv(csv_file)
    df = df[df.text != None]
    lista = [float(item.split(',')[0]) for item in df['loc']]
    listb = [float(item.split(',')[1]) for item in df['loc']]
    df['lat'] = lista
    df['lon'] = listb
    df.drop('Unnamed: 0', axis='columns', inplace=True)
    df.to_csv('data/hotel_review_cleaned.csv')
    return df

def add_sentiment(df):
    first = pd.read_csv('first_403.csv', header=None)
    rest = pd.read_csv('rest.csv', header=None)
    complete = pd.concat([first, rest], axis=0)
    complete.to_csv('data/sentiment_results.csv')
    df['sentiment'] = complete[0].tolist()
    df.to_csv('data/hotel_review_sent.csv')
    return df


df = clean_for_tableau('data/hotel_reviews.csv')
df = add_sentiment(df)