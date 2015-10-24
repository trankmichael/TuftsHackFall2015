from urllib2 import urlopen
from bs4 import BeautifulSoup
import json

import pandas as pd
from HTMLParser import HTMLParser

key = "AFBD081FB72F44529BF24D87BBA2F90D"

url_template1 = "http://api.tripadvisor.com/api/partner/2.0/map/{lat_lng}/geos?key=AFBD081FB72F44529BF24D87BBA2F90D"
url_template2 = "http://api.tripadvisor.com/api/partner/2.0/location/{location}/hotels?key=AFBD081FB72F44529BF24D87BBA2F90D"
url_template3 = "http://api.tripadvisor.com/api/partner/2.0/location/{hotel}/reviews?key=AFBD081FB72F44529BF24D87BBA2F90D"

coords = ["42.33141,-71.099396"]

length = 10

for coord in coords:
	url = url_template1.format(lat_lng=coord)
	html = urlopen(url)
	locations_dict = json.load(html)

	locations = [location['location_id'] for location in locations_dict['data']]

	for location in locations:
		url = url_template2.format(location=location)
		html = urlopen(url)
		hotel_dict = json.load(html)

		hotels = [hotel['location_id'] for hotel in hotel_dict['data']]

		reviews_df = pd.DataFrame()

		for hotel in hotels:
			url = url_template3.format(hotel=hotel)
			html = urlopen(url)
			reviews_dict = json.load(html)

			ids = (review_id['id'] for review_id in reviews_dict['data'])
			ratings = (review_id['rating'] for review_id in reviews_dict['data'])

			text = (review_id['text'] for review_id in reviews_dict['data'])

 			# location_ids.append(reviews_dict['data'][0]['location_id'])
	 		# text.append(reviews_dict['data'][0]['text'])

	 		hotel_df = pd.DataFrame([ids,ratings,text])

	 		reviews_df = reviews_df.append(hotel_df, ignore_index = True)










		# for i in range(length):
		# 	ids.append (location_dict['data'][i]['id'])
 	# 		location_ids.append(location_dict['data'][i]['location_id'])
	 # 		text.append(location_dict['data'][i]['text'])



# # need location array to loop through

# locations = ["695745"]

# reviews_df = pd.DataFrame()

# for location in locations:
# 	url = url_template.format(location=location)
# 	html = urlopen(url)
# 	location_dict = json.load(html)

# 	unique_id = location_dict['data'][0]['id']
# 	location = [location_dict['data'][0]['location_id']
# 	text = text for text in location_dict['data'][0]['text']

# print text






