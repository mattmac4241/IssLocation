import json
import urllib2
from helpers import get_page

#return the latitude and longitude of the iss
def get_location():
    data = get_page('http://api.open-notify.org/iss-now.json')
    location = data['iss_position']
    longitude = get_longitude(location)
    latitude = get_latitude(location)
    return {'lat':latitude,'long':longitude}

#return the longitude
def get_longitude(data):
    return data['longitude']

#return the latitude
def get_latitude(data):
    return data['latitude']



