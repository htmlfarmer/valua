import urllib
import urllib2
import socket # needed for timeout
import re
import xml.etree.ElementTree as ET

# TODO: request API + https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module

#harmonic mean
#from scipy import stats
#import numpy

ZILLOW_KEY = "X1-ZWz18uigx8hcej_1acr8"
GOOGLE_API_KEY = "AIzaSyAD3AiNwlR6x-rHjYGbp277Whqf3t6LKvQ"
US_CENSUS_KEY = "9d4c29e072ec00a326361a8146c792f465d49186"

# goal is to compare yelp with ZILLOW
def MAIN ():
    
    locations = [\
        {"address" : "0 Treasure Island Dr", "citystatezip" : "Aptos, CA 95003"}, \
        {"address" : "412 6th Ave", "citystatezip" : "Tacoma, WA 98402"}, \
        {"address" : "2028 S 7th St", "citystatezip" : "Tacoma, WA 98405"}, \
        {"address" : "708 S Junett St", "citystatezip" : "Tacoma, WA 98405"}, \
        {"address" : "1111 Morse Ave SPC 168", "citystatezip" : "Sunnyvale, CA 94089"}, \
        {"address" : "251 N 19TH St", "citystatezip" : "San Jose, CA 95112"}, \
        {"address" : "252 Sonora Pass Rd", "citystatezip" : "Vallejo, CA 94589"}, \
        {"address" : "628 2nd St", "citystatezip" : "Rodeo, CA 94572"}, \
        {"address" : "339 W Chanslor Ave", "citystatezip" : "Richmond, CA 94801"}, \
        {"address" : "1468 Sandpiper Spit", "citystatezip" : "Richmond, CA 94801"}, \
        {"address" : "834 Loma Prieta Dr", "citystatezip" : "Aptos, CA 95003"}, \
        {"address" : "210 E 1st Street", "citystatezip" : "Moscow, ID"}]
        
    for location in locations :
        print location
        CENSUS_ECONOMIC()
        #html = ZILLOW(location["address"], location["citystatezip"])
        #PARSE_ZILLOW_XML(html)
        #location = CENSUS_GEOCODE(location["address"], location["citystatezip"])
        #GOOGLE_PLACES(location)


# https://www.census.gov/data/developers/data-sets/economic-census.html
# https://api.census.gov/data/2012/ewks/variables.html
# EXAMPLES https://api.census.gov/data/2012/ewks/examples.html
def CENSUS_ECONOMIC ():
    FIELDS = "RCPTOT,OPTAX"
    NAICS2012 = "71" # 71 ARTS AND ENTERTAINMENT
    url = "https://api.census.gov/data/2012/ewks?get=" + FIELDS + "&for=state:*&NAICS2012=" + NAICS2012 \
    + "&key=" + US_CENSUS_KEY
    text = GET_REQUEST(url)
    print text
    return text

def ZILLOW(address, citystatezip):
    # FAQ: https://www.zillow.com/howto/api/GetSearchResults.htm (main starting point)
    # FAQ: https://www.zillow.com/howto/api/GetUpdatedPropertyDetails.htm
    # http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=<ZWSID>&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA
    print "LOOKUP ADDRESS: " + address + " " + citystatezip
    address_url = address.replace(" ", "+")
    citystatezip_url = citystatezip.replace(" ", "+")
    url = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=" + ZILLOW_KEY + "&address=" + address_url + "&citystatezip=" + citystatezip_url
    #print "LOOKUP: " + url
    html = GET_REQUEST(url)
    return html

# http://ec.europa.eu/eurostat/web/json-and-unicode-web-services/getting-started/rest-request
# DATABASE: http://ec.europa.eu/eurostat/data/database
def EUROSTAT(latitude, logitude):
    #health
    #education
    #social
    return

def GOOGLE_PLACES_DETAILS(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + place_id + "&key=" + GOOGLE_API_KEY
    json = GET_REQUEST(url)
    return json

def GOOGLE_PLACES_ID(json):
    ids = []
    start = json.find("\"places_id\" : ")
    while start != -1:
        end = json.find(",", start)
        place_id = json[start+14:end]
        ids = ids.append(place_id)
        start = json.find("\"places_id\" : ", end) # start = last end
    print ids
    return ids

def GOOGLE_PLACES_RATINGS(json):
    ratings = []
    start = json.find("\"rating\" : ")
    while start != -1:
        end = json.find(",", start)
        rating = json[start+11:end]
        ratings.append(float(rating))
        start = json.find("\"rating\" : ", end) # start = last end
    print ratings
    return ratings

def GOOGLE_PLACE_TYPES(json):
    types = ""
    start = json.find("\"types\" : [")
    while start != -1:
        end = json.find("],", start)
        typed = json[start+11:end]
        types = types + typed + ","
        start = json.find("\"types\" : ", end) # start = last end
    print types[0:len(types)-1].replace('\n', '').replace(' ', '')
    return types[0:len(types)-1].replace('\n', '').replace(' ', '')

# GOOGLE PLACES API https://developers.google.com/places/web-service/
# https://maps.googleapis.com/maps/api/place/textsearch/json?query=123+main+street&key=YOUR_API_KEY
def GOOGLE_PLACES(location):
    if location["latitude"] != None and location["longitude"] != None:
        radius = "5000"
        #types = "food"
        # &keyword=vegetarian
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" \
        + location["latitude"] + "," + location["longitude"] + "&radius=" + radius + "&name=" \
        + "&sensor=false&key=" + GOOGLE_API_KEY
        json = GET_REQUEST(url)
        GOOGLE_PLACES_RATINGS(json)
        GOOGLE_PLACE_TYPES(json)
        print json
        return json
    else:
        return None

def PARSE_ZILLOW_XML(text):
    root = ET.fromstring(text)
    for zpid in root.iter('zpid'):
        zpid = zpid.text
    for address in root.iter('street'):
        address = address.text
    for citystatezip in root.iter('citystatezip'):
        citystatezip = citystatezip.text
    for zestimate in root.iter('amount'):
        if zestimate.text is not None:
            zestimate = int(zestimate.text)
    for low in root.iter('low'):
        if low.text is not None:
            low = int(low.text)
    for high in root.iter('high'):
        if high.text is not None:
            high = int(high.text)
    for latitude in root.iter('latitude'):
        latitude = latitude.text
    for longitude in root.iter('longitude'):
        longitude = longitude.text
    hmean = 0 #stats.hmean([ zestimate, high, low ])
    gmean = 0 #stats.gmean([ zestimate, high, low ])
    doc = {"zpid" : zpid, "price" : zestimate, "low" : low, "high" : high, \
            "latitude" : latitude, "longitude" : longitude, "citystatezip" : citystatezip, \
            "address" : address, "hmean" : hmean, "gmean" : gmean}
    print doc
    return doc

def VALUA (house):
    print "VALUA.ORG"
    # 1.) COMPARISON
    print "1.) COMPARISON"
    print "2.) COST (NEW)"
    print "3.) INCOME (RENTAL)"
    return

def VALUA_RADAR(address, latitude, longitude):
    # function collects all the data needed on a particular address or lat/lng
    return

def VALUA_TITLE (address, latitude, longitude):
    print "PROPERTY TITLE EVALUATION: https://en.wikipedia.org/wiki/Title_(property)"
    return

def VALUA_LOAN (address, latitude, longitude):
    # BARROWERS
    # LENDERS
    # MONTHLY PAYMENT
    print "PROPERTY LOAN EVALUATION: https://en.wikipedia.org/wiki/Mortgage_loan"

# https://www.census.gov/data/developers/data-sets/economic-indicators.html
def CENSUS_HOUSING ():
    return

# https://www.census.gov/data/developers/data-sets/international-database.html
def CENSUS_INTERNATIONAL (location):
    return

# ACTUAL https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html
# PROJECTED https://www.census.gov/data/developers/data-sets/popest-popproj/popproj.html
def CENSUS_POPULATION ():
    population = 0
    return population

# FAQ: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html#_Toc379292359
# example: https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=4600+Silver+Hill+Rd%2C+Suitland%2C+MD+20746&benchmark=9&format=json
def CENSUS_GEOCODE (address, citystatezip):
    address = address.replace(" ", "+")
    address = address.replace(",", "%2C")
    citystatezip = citystatezip.replace(" ", "+")
    citystatezip = citystatezip.replace(",", "%2C")
    url = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=" + address + "+" + citystatezip + "&benchmark=9&format=json"
    json = GET_REQUEST(url).replace(" ", "")
    # find the logitude and latitude in the JSON reply
    start = json.find("\"x\":")
    if(start != -1):
        end = json.find(",", start)
        longitude = json[start+4:end]
        start = json.find("\"y\":")
        end = json.find("}", start)
        latitude = json[start+4:end]
    else:
        longitude = None
        latitude = None
    geocode = {"longitude" : longitude, "latitude" : latitude}
    print geocode
    return geocode

# https://www.census.gov/data/developers/data-sets/economic-indicators.html
def CENSUS_HOUSING ():
    return

# https://www.census.gov/data/developers/data-sets/Health-Insurance-Statistics.html
# https://www.census.gov/geographies/reference-files/2016/demo/popest/2016-fips.html
def CENSUS_HEALTH():
    # SAN JOSE:
    # BERKELY:
    # OAKLAND:
    # VALEJO: 
    # SAN MATAO: 
    # CHICAGO: 
    # MOSCOW: 
    # NEW YORK:
    # BROOKLYN:
    # QUEENS:
    # BRONX:
    # SEATTLE:
    # PORTLAND: 
    return

def GET_REQUEST(address):
    timeout = 60
    socket.setdefaulttimeout(timeout)
    user_agent = 'VALUA. + RESEARCH SCIENCE (Linux; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url = address, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

MAIN()
