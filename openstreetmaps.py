import xml.etree.ElementTree as ET
from request import REQUEST


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
