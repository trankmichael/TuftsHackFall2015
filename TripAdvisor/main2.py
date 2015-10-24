from urllib2 import urlopen
from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
import pandas as pd
from HTMLParser import HTMLParser

key = "AFBD081FB72F44529BF24D87BBA2F90D"

near_locations = "http://api.tripadvisor.com/api/partner/2.0/map/{lat_lng}/geos?key=" + key
best_hotels = "http://api.tripadvisor.com/api/partner/2.0/location/{id}/hotels?key=" + key
hotel_reviews = "http://api.tripadvisor.com/api/partner/2.0/location/{hotel}/reviews?key=" + key
coords = ["42.33141,-71.099396"]

length = 10

def get_loc_ids(geographic_locs):
    return [x['location_id'] for x in geographic_locs['data']]

def get_hotels(loc_ids):
    all_hotels = []
    for loc in loc_ids:
        data = requests.get(best_hotels.format(id=loc)).json()['data']
        hotels = [{'id': x['location_id']} for x in data]
        all_hotels.extend(hotels)
    return all_hotels


def get_reviews(hotel):
    list_of_reviews = []
    for hotel in hotels:
        data = requests.get(hotel_reviews.format(hotel=hotel['id'])).json()['data']
        for rev in data:
            review = {'id': rev['id'], 'rating': rev['rating'], 'text': rev['text']}
            list_of_reviews.append(review)
    return list_of_reviews



geo = requests.get(near_locations.format(lat_lng=coords[0])).json()
loc_ids = get_loc_ids(geo)
hotels = get_hotels(loc_ids)
hotel_review = get_reviews(hotels)
df = pd.DataFrame(hotel_review)
df['loc'] = coords[0]