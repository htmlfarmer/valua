import urllib
import urllib2
import socket # needed for timeout
import re
import json
import sys
import xml.etree.ElementTree as ET

# harmonic mean
from scipy import stats
import numpy



ZILLOW_KEY = "X1-ZWz18uigx8hcej_1acr8"

def MAIN ():
    locations = [{"address" : "2923 71st Street", "citystatezip" : "Woodridge, IL"}, \
                {"address" : "321 N. Howard St.", "citystatezip" : "Moscow, ID"}, \
                {"address" : "210 E 1st Street", "citystatezip" : "Moscow, ID"}]
    for location in locations :
        print location
        html = ZILLOW(location["address"], location["citystatezip"])
        PARSE_XML(html)


def ZILLOW_ESTIMATE():
    url = "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=" + ZILLOW_KEY + "&zpid=" + PROPERTY_ID
    html = GET_REQUEST(url)
    if(regex):
        matcher = re.compile(regex)
        match = matcher.search(html).group()
        print match
    else:
        print html
    return html

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

def PARSE_XML(text):
    root = ET.fromstring(text)
    for zpid in root.iter('zpid'):
        zpid = zpid.text
    for address in root.iter('street'):
        address = address.text
    for citystatezip in root.iter('citystatezip'):
        citystatezip = citystatezip.text
    for zestimate in root.iter('amount'):
        zestimate = int(zestimate.text)
    for low in root.iter('low'):
        low = int(low.text)
    for high in root.iter('high'):
        high = int(high.text)
    for latitude in root.iter('latitude'):
        latitude = latitude.text
    for longitude in root.iter('longitude'):
        longitude = longitude.text
    hmean = stats.hmean([ zestimate, high, low ])
    gmean = stats.gmean([ zestimate, high, low ])
    doc = {"zpid" : zpid, "price" : zestimate, "low" : low, "high" : high, \
            "latitude" : latitude, "longitude" : longitude, "citystatezip" : citystatezip, \
            "address" : address, "hmean" : hmean, "gmean" : gmean}
    print doc
    return doc

def ZILLOW_ESTIMATE():
    url = "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=" + ZILLOW_KEY + "&zpid=" + PROPERTY_ID
    html = GET_REQUEST(url)
    if(regex):
        matcher = re.compile(regex)
        match = matcher.search(html).group()
        print match
    else:
        print html
    return html

def VALUA_DETAILS():
    zillow_details = "http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=" + ZILLOW_KEY + "&zpid=" + PROPERTY_ID
    html = GET_REQUEST(zillow_details)
    if(regex):
        matcher = re.compile(regex)
        match = matcher.search(html).group()
        print match
    else:
        print html
    return html

def GET_REQUEST(address):
    timeout = 60
    socket.setdefaulttimeout(timeout)
    user_agent = 'VALUA. + RESEARCH (Linux; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url = address, headers = headers)
    response = urllib2.urlopen(req)
    content = response.read()
    return content

MAIN()
