from iss import get_location
from gmaps import get_location_by_long_lat,get_city,no_location

iss =  get_location()
latitude = iss['lat']
longitude = iss['long']
location = get_location_by_long_lat(longitude,latitude)
if(no_location(location) == True):
    print "Currently located above an ocean"
else:
    print get_city(location)
