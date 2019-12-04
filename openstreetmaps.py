import xml.etree.ElementTree as ET
from request import REQUEST

# XML EXAMPLE
# EXAMPLE https://nominatim.openstreetmap.org/search?q=135+pilkington+avenue,+birmingham&format=xml&polygon=1&addressdetails=1
def OPEN_XML_GEOCODE(address):
    address = address.replace(" ", "+")
    import re
    address = re.sub('\(.*\)', '', address) # replace everything between () with nothing
    address = re.sub('\+{2,}', '+', address)
    url = "https://nominatim.openstreetmap.org/search?q=" + address + "&format=xml&polygon=1&addressdetails=1"
    XML = REQUEST(url)
    # lat='37.4851868' lon='-122.1478019
    start = XML.find("lat=")
    end = XML.find("\' ", start)
    latitude = XML[start+5:end].replace('\n', '').replace(' ', '')
    start = XML.find("lon=")
    end = XML.find("\' ", start)
    longitude = XML[start+5:end].replace('\n', '').replace(' ', '')
    geocode = {"longitude" : longitude, "latitude" : latitude}
    return geocode

# GEO JSON
# API https://nominatim.org/release-docs/develop/api/Search/
# EXAMPLE: https://nominatim.openstreetmap.org/?addressdetails=1&q=bakery+in+berlin+wedding&format=json&limit=1
def OPEN_GEOCODE(address):
    address = address.replace(" ", "+")
    address = address.replace("(", "+")
    address = address.replace(")", "+")
    url = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + address + "&format=json&limit=1"
    json = REQUEST(url)
    start = json.find("\"lat\":\"")
    end = json.find("\",", start)
    latitude = json[start+7:end].replace('\n', '').replace(' ', '')
    start = json.find("\"lon\":\"")
    end = json.find("\",", start)
    longitude = json[start+7:end].replace('\n', '').replace(' ', '')
    geocode = {"longitude" : longitude, "latitude" : latitude}
    return geocode


def osm_features(latlon):
    #https://www.openstreetmap.org/query?lat=-19.9168&lon=-43.9332
    return

def osm_search(keywords):
    name = keywords
    keywords = keywords.replace(" ", "+") # replace spaces with +'s
    keywords = keywords.replace("\t", "%09") # replace tabs
    url = 'https://nominatim.openstreetmap.org/search.php?q=' + keywords + '&polygon_geojson=1&viewbox='
    html = REQUEST(url)
    # from the html look at the output and study which output is correct to get the internal data from the search

    root = ET.fromstring(html)
    # first search result xpath
    # xpath = //*[@id="searchresults"]/div[1]/a
    xpath = './/*[@id="searchresults"]/div[' + str(1) + ']/a'
    search_result = root.find(xpath)  # was there a search result?

    return html
