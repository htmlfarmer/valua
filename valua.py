# by Asher Martin
# November 2019
# About: this program is designed to help search for news and evaluate it.

# Warning: The xml.etree.ElementTree module is not secure against maliciously constructed data.
# If you need to parse untrusted or unauthenticated data see XML vulnerabilities.

#import urllib
#import re
#import xml.etree.ElementTree as ET

import census
import google
import zillow
import wikipedia
import openstreetmaps
import time
import datetime

"""

"""

print "==================================================="
print "  REPORT # " , datetime.datetime.now()
print "    DATE : ", datetime.date.today().strftime("%B") + " " + datetime.date.today().strftime("%d") + ", " + datetime.date.today().strftime("%Y")
print "==================================================="

from request import REQUEST

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
    wikipedia.findNews(html)
    return html


def writefile(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()


# read in a file and print it and process the data
def readfile(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()  # preprocess line
            #print (line)
            lines.append(line)  # storing everything in memory!
    return lines

#############################################
#          MAIN PROGRAM OUTLINE
#############################################


def MAIN ():

# READ IN ALL SP500 and NASDAQ INFO
    nasdaq = readfile("nasdaq.txt")
    sp100 = readfile("sp500.txt")

#    openstreetmaps.osm_search("moscow idaho")

# READ WIKIPEDIA WEBSITE URLS

    urls = [ \
        {"type": "stock", "address": "https://en.wikipedia.org/wiki/Apple_Inc."}, \
        #{"address": "https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=APPLE+INC.%09AAPL&title=Special%3ASearch&go=Go&ns0=1"}, \
        #{"address": "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"}, \
        #{"address": "https://www.eia.gov/naturalgas/crudeoilreserves/"}, \
        {"type": "news", "address": "https://en.wikipedia.org/wiki/2019"}, \
        {"type": "other", "address": "https://www.ci.moscow.id.us/507/Daily-Activity-Log"}, \
        {"type": "quora", "address": "https://www.quora.com/topic/Portland-OR"}, \
        {"type": "personal", "address": "https://ashercmartin.wordpress.com/links/"}, ]

    # search wikipedia for each stock in the nasdaq
    # and find the most relevant page

    for stock in nasdaq:
        print stock
        wikipedia.wiki_research(stock)
    """"
    for stock in sp100:
        print stock
        wikipedia.wiki_research(stock)

    for url in urls:
        print url
        html = GET_REQUEST(url["address"])
        writefile("file.html", html)
        if url["type"] == "stock":
            wikipedia.wiki_stock(html)
        elif url["type"] == "news":
            wikipedia.wiki_news(html),  # do not use ()
        elif url["type"] == "quora":
            print "quora"
        else:
            print "other"
    """

# GET ALL THE LOCATION INFORMATION FROM THE HTML FILE

"""
    locations = [ \
        {"address": "2923 71st Street", "citystatezip": "Woodridge, IL 60517"}, \
        {"address": "210 E. 1st Street", "citystatezip": "Moscow, ID 83843"}, \
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
