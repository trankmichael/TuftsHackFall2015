from urllib2 import urlopen
from bs4 import BeautifulSoup

import pandas as pd

url_coordinates = "http://www.infoplease.com/ipa/A0001796.html"
html_coordinates = urlopen(url_coordinates)
soup = BeautifulSoup(html_coordinates, 'html.parser')


data_rows = soup.findAll('tr')[3:-1] 

coordinate_data = [[td.getText() for td in data_rows[i].findAll('td')[1:-1]]
                		for i in range(len(data_rows))]

print coordinate_data