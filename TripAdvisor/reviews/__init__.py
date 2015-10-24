from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

__author__ = 'mumbosauce'
key = "AFBD081FB72F44529BF24D87BBA2F90D"
near_locations = "http://api.tripadvisor.com/api/partner/2.0/map/{lat_lng}/geos?key=" + key
best_hotels = "http://api.tripadvisor.com/api/partner/2.0/location/{id}/hotels?key=" + key
hotel_reviews = "http://api.tripadvisor.com/api/partner/2.0/location/{hotel}/reviews?key=" + key
url_coordinates = "http://www.infoplease.com/ipa/A0001796.html"
html_coordinates = urlopen(url_coordinates)
soup = BeautifulSoup(html_coordinates, 'html.parser')


def us_coords():
    data_rows = soup.findAll('tr')[3:]
    coordinate_data = [[td.getText() for td in data_rows[i].findAll('td')[1:-1]] for i in range(len(data_rows) - 1)]
    coords = [format_lat_long(cd) for cd in coordinate_data]
    return coords


def format_lat_long(cd):
    return cd[0] + "." + cd[1] + ",-" + cd[2] + "." + cd[3]


def get_loc_ids(geographic_locs):
    return [x['location_id'] for x in geographic_locs['data']]


def get_hotels(loc_ids):
    all_hotels = []
    for loc in loc_ids:
        data = requests.get(best_hotels.format(id=loc)).json()['data']
        hotels = [{'id': x['location_id']} for x in data]
        all_hotels.extend(hotels)
    return all_hotels


def get_reviews(hotels):
    list_of_reviews = []
    for hotel in hotels:
        data = requests.get(hotel_reviews.format(hotel=hotel['id'])).json()['data']
        for rev in data:
            review = {'id': rev['id'], 'rating': rev['rating'], 'text': rev['text']}
            list_of_reviews.append(review)
    return list_of_reviews


def get_hotel_reviews():
    coords = us_coords()
    all_reviews = pd.DataFrame()
    for coord in coords:
        geo = requests.get(near_locations.format(lat_lng=coord)).json()
        loc_ids = get_loc_ids(geo)
        hotels = get_hotels(loc_ids)
        hotel_review = get_reviews(hotels)
        df = pd.DataFrame(hotel_review)
        df['loc'] = coord
        all_reviews = all_reviews.append(df, ignore_index=True)
    return all_reviews
