#import urllib
#import re
#import xml.etree.ElementTree as ET
import census
import google
import zillow

# TODO: request API + https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module

#harmonic mean
#from scipy import stats
#import numpy

# COLLABORATORS:
# MIT/HARVARD https://atlas.media.mit.edu/en/rankings/product/sitc/
# ASTOR/NASA https://lpdaac.usgs.gov/dataset_discovery/aster/aster_products_table/ast_09xt_v003

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
        #census.CENSUS_ECONOMIC()
        #html = zillow.ZILLOW(location["address"], location["citystatezip"])
        #zillow.PARSE_ZILLOW_XML(html)
        # doesn't work for international
        # location = census.CENSUS_GEOCODE(location["address"], location["citystatezip"])
        location = google.GOOGLE_GEOCODE(location["address"] + " " + location["citystatezip"])
        google.GOOGLE_PLACES(location)

# http://ec.europa.eu/eurostat/web/json-and-unicode-web-services/getting-started/rest-request
# DATABASE: http://ec.europa.eu/eurostat/data/database
def EUROSTAT(latitude, logitude):
    #health
    #education
    #social
    return

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

MAIN()
