from urllib2 import urlopen
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn.cluster import KMeans
from geopy.geocoders import Nominatim

#geolocator = Nominatim()
#
#so_cal = ['Los Angeles', 'San Diego', 'Anaheim', 'Long Beach', 'Las Vegas']
#nor_cal = ['Oakland', 'Reno', 'Sacramento', 'San Jose', 'San Francisco']
#sun_corridor = ['Phoenix', 'Tucson']
#cascadia = ['Portland', 'Seattle', 'Vancouver']
#fort_range = ['Albuquerque', 'Santa Fe', 'Colorado Springs', 'Denver']
#others = ['Alaska', 'Hawaii']
#
#texas_triangle = ['Austin', 'Dallas', 'Houston', 'San Antonio']
#north_east = ['Boston', 'New York', 'Philadelphia', 'Baltimore', 'Washington D.C.']
#gulf_coast = ['Houston', 'New Orleans', 'Baton Rouge']
#great_lakes = ['Chicago', 'Detroit', 'Pittsburgh', 'Cleveland', 'Minneapolis', 'St. Louis', 'Indianapolis']
#florida = ['Miami', 'Orlando', 'Tampa', 'Jacksonville']
#pied_atlantic = ['Atlanta', 'Birmingham', 'Raleigh-Durham', 'Charlotte']
#
#def distance(x, y, x_1, y_1):
#    return (x - x_1)**2 + (y - y_1)**2
#
#def calculate_center(cities):
#    n = len(cities)
#    lat_avg = sum([geolocator.geocode(city).latitude for city in cities]) / float(n)
#    lon_avg = sum([geolocator.geocode(city).longitude for city in cities]) / float(n)
#    return (lat_avg, lon_avg)
#
#def build_lats_lng(region):
#    for [(geolocator.geocode(city).latitude, geolocator.geocode(city).long) for city in region]
#
#mega_regions = [texas_triangle, so_cal, nor_cal, sun_corridor, cascadia, fort_range, north_east, gulf_coast, florida, great_lakes, pied_atlantic]
#mega_regions = [build_lats_lngs(region) for region in mega_regions]
#region_centroids = [calculate_center(mega_regions[i]) for i in xrange(len(mega_regions))]
    

df = pd.read_csv('data/hotel_review_sent.csv')
means = df.groupby(['loc'])['sentiment','rating'].mean().reset_index()
locs = [(loc.split(',')[0], loc.split(',')[1]) for loc in means['loc']]
k_means = KMeans(n_clusters=8)
k_means.fit(locs)
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_ 
print(y)

#trace0 = go.Scatter(
#    y=means['rating'],
#    x=means['sentiment'],
#    mode='markers'
#)
#
## #trace1 = go.Scatter(
## #    x=range(len(means)),
## #    y=means['rating']
## #)
#data = [trace0]
#plot_url = py.plot(data, filename='sentiment')
