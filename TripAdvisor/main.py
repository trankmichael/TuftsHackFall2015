from urllib2 import urlopen
from bs4 import BeautifulSoup
import json

import pandas as pd
from HTMLParser import HTMLParser

key = "AFBD081FB72F44529BF24D87BBA2F90D"

url_template1 = "http://api.tripadvisor.com/api/partner/2.0/map/{lat_lng}/geos?key=AFBD081FB72F44529BF24D87BBA2F90D"
url_template2 = "http://api.tripadvisor.com/api/partner/2.0/location/{location}/reviews?key=AFBD081FB72F44529BF24D87BBA2F90D"
coords = ["42.33141,-71.099396"]

length = 10

for coord in coords:
	url = url_template1.format(lat_lng=coord)
	html = urlopen(url)
	location_dict = json.load(html)

	locations = []
	for i in range(length):
		locations.append(location_dict['data'][i]['location_id'])

print locations

	# for location in locations:
	# 	print location
	# 	url = url_template2.format(location=location)
	# 	html = urlopen(url)
	# 	location_dict = json.load(html)
	# 	ids = []
	# 	location_ids = []
	# 	text = []



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






