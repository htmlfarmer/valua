#import urllib
#import re
#import xml.etree.ElementTree as ET

import census
import google
import zillow

import time
import datetime

#print "Time in seconds since the epoch: %s" %time.time()
print "REPORT: " , datetime.datetime.now()
print "  DATE: ", datetime.date.today().strftime("%B") + " " + datetime.date.today().strftime("%d") + ", " + datetime.date.today().strftime("%Y")

from request import GET_REQUEST

"""
# Do a Wikipedia Lookup Based on geolocation (Cape Cod, MA) http://api.geonames.org/findNearbyWikipedia?lat=41.618116&lng=-70.485361&username=demo
wikihtml = GET_REQUEST("http://api.geonames.org/findNearbyWikipedia?lat="+ str(lat) +"&lng="+ str(lng) + "&username=asolr")
wiki = ET.fromstring(wikihtml) # if you need the xml data type
print ET.tostring(wiki)
"""



# TODO: request API + https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module

# COLLABORATORS:

# MAIN SEARCH ENGINE
def SEARCH(url):

    print url
    html = GET_REQUEST(url)
    print html
    return html

# MAIN PROGRAM OUTLINE
def MAIN ():

    urls = [ \
        {"address": "https://en.wikipedia.org/wiki/2019"}, \
        {"address": "https://www.ci.moscow.id.us/507/Daily-Activity-Log"}, \
        {"address": "https://ashercmartin.wordpress.com/links/"}, ]

    for url in urls:
        print url
        SEARCH(url["address"])

"""
    locations = [ \
        {"address": "2923 71st Street", "citystatezip": "Woodridge, IL 60517"}, \
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
        #census.CENSUS_ECONOMIC()
        html = zillow.ZILLOW(location["address"], location["citystatezip"])
        zillow.PARSE_ZILLOW_XML(html)
        # doesn't work for international
        location = census.CENSUS_GEOCODE(location["address"], location["citystatezip"])
        # google started requiring payment codes!?
        #location = google.GOOGLE_GEOCODE(location["address"] + " " + location["citystatezip"])
        #google.GOOGLE_PLACES(location)
"""

# http://ec.europa.eu/eurostat/web/json-and-unicode-web-services/getting-started/rest-request
# DATABASE: http://ec.europa.eu/eurostat/data/database

MAIN()
