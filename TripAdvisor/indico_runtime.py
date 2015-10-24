import pandas as pd
import indicoio
import cProfile
from pprint import pprint
import csv

indicoio.config.api_key = 'bbc6aca3c1564961ba2f0ee5dc81f32f'
df = pd.read_csv('data/hotel_reviews.csv')
indicoio.sentiment_hq([
    "indico is so easy to use!",
    "everything is awesome!"
])
