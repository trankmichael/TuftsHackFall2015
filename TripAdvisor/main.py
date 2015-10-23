from urllib2 import urlopen
from bs4 import BeautifulSoup
import json

import pandas as pd
from HTMLParser import HTMLParser

url = "http://api.tripadvisor.com/api/partner/2.0/location/{location}/reviews?key=AFBD081FB72F44529BF24D87BBA2F90D"
key = "AFBD081FB72F44529BF24D87BBA2F90D"

# need location array to loop through

for location in locations
	url = url_template.format(team=team)
    html = urlopen(url)

    location_dict = json.load(html)
    location_df = pd.DataFrame()


