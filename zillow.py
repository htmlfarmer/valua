from request import GET_REQUEST
import xml.etree.ElementTree as ET

ZILLOW_KEY = "X1-ZWz18uigx8hcej_1acr8"

def PARSE_ZILLOW_XML(text):
    if "Error:" in text:
        return None
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
