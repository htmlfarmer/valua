import urllib
import urllib2
import socket # needed for timeout
import re
import json
import sys
import xml.etree.ElementTree as ET

# harmonic mean
#from scipy import stats
#import numpy

test = '<tr ng-repeat="measure in component.measures" class="measure ng-scope" style="">"Percentage of adults reporting fair or poor health (age-adjusted)"><td class="target mobile-drop ng-binding" ng-bind-html="measure.displayTarget">12%</td></tr>'

ZILLOW_KEY = "X1-ZWz18uigx8hcej_1acr8"

# goal is to compare yelp with ZILLOW
def MAIN ():
    locations = [{"address" : "412 6th Ave", "citystatezip" : "Tacoma, WA 98402"},
        {"address" : "2028 S 7th St", "citystatezip" : "Tacoma, WA 98405"}, \
        {"address" : "708 S Junett St", "citystatezip" : "Tacoma, WA 98405"}, \
        {"address" : "1111 Morse Ave SPC 168", "citystatezip" : "Sunnyvale, CA 94089"}, \
        {"address" : "251 N 19TH St", "citystatezip" : "San Jose, CA 95112"}, \
        {"address" : "252 Sonora Pass Rd", "citystatezip" : "Vallejo, CA 94589"}, \
        {"address" : "628 2nd St", "citystatezip" : "Rodeo, CA 94572"}, \
        {"address" : "339 W Chanslor Ave", "citystatezip" : "Richmond, CA 94801"}, \
        {"address" : "1468 Sandpiper Spit", "citystatezip" : "Richmond, CA 94801"}, \
        {"address" : "0 Treasure Island Dr", "citystatezip" : "Aptos, CA 95003"}, \
        {"address" : "834 Loma Prieta Dr", "citystatezip" : "Aptos, CA 95003"}, \
        {"address" : "210 E 1st Street", "citystatezip" : "Moscow, ID"}]

    for location in locations :
        print location
        #html = ZILLOW(location["address"], location["citystatezip"])
        #PARSE_ZILLOW_XML(html)

    health_locations = [{"state" : "california", "county" : "santa-clara"}] #, {"state" : "idaho", "county" : "latah"}]

    for health in health_locations :
        print health
        html = CDC_HEALTH(health["state"], health["county"])

def CDC_HEALTH_PARSE(html):
    #DISPLAY(html)
    print html
    founds = re.findall('<tr*>(.*?)</tr>',str(html))
    for found in founds:
        print(found)
    # matcher = re.compile(regex)
    # match = matcher.search(html).group()
    return html

def CDC_HEALTH(state, county):
    url = "http://www.countyhealthrankings.org/app/" + state + "/2017/rankings/" + county + "/county/outcomes/overall/snapshot"
    #html = GET_REQUEST(url)
    CDC_HEALTH_PARSE(test)
    return html

def DISPLAY(html): #experimental doesn't work yet
    print re.sub("<.*?>", "", html)

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
    user_agent = 'VALUA. + RESEARCH SCIENCE (Linux; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url = address, headers = headers)
    response = urllib2.urlopen(req)
    content = response.read()
    text = content.decode() # maybe remove
    return text

MAIN()
