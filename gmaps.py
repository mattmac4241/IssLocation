from helpers import get_page,get_key

key = get_key()

#get location from zipcode
def get_location_by_zipcode(zipcode):
    data = get_page('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (zipcode,key))
    return data

#get location by using longitude and latitude
def get_location_by_long_lat(longitude,latitude):
    data = get_page('https://maps.googleapis.com/maps/api/geocode/json?address=%s+%s&key=%s'% (latitude,longitude,key))
    return data

#get city from data
def get_city(data):
    return data['results'][0]['formatted_address']

#no location
def no_location(data):
    if data['results'] == []:
        return True
    else:
        return False   

