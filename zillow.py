import urllib
import urllib2
import socket # needed for timeout
import re
import json
import sys
import xml.etree.ElementTree as ET

ZILLOW_KEY = "X1-ZWz18uigx8hcej_1acr8"
PROPERTY_ID = "48749425"

# About: Get Remote Content
url = "http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=" + ZILLOW_KEY + "&zpid=" + PROPERTY_ID
regex = "" # for static regex

if(len(sys.argv) > 1):
    url = sys.argv[1]
    if(len(sys.argv) > 2):
        regex = sys.argv[2]
else: # requires "http://" before
    url= "http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=" + ZILLOW_KEY + "&zpid=" + PROPERTY_ID


import xml.etree.ElementTree as ET

def ZILLOW(): #(address, citystatezip):
    # http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=<ZWSID>&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA
    address = "2923+71st+street"
    citystatezip = "Woodridge+IL"
    url = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=" + ZILLOW_KEY + "&address=" + address + "&citystatezip=" + citystatezip
    print "LOOKUP: " + url
    xml = GET_REQUEST(url)
    if(regex):
        matcher = re.compile(regex)
        match = matcher.search(html).group()
        #print match
    else:
        #print xml
        ZILLOW_XML(xml)
    return xml

def ZILLOW_XML(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    #for child in root:
    #    print (child.tag, child.attrib)

def VALUA():
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

# TEST CODE GOES HERE

#VALUA()
ZILLOW()
