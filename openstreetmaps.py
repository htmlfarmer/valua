from request import REQUEST

def osm_search(keywords):
    name = keywords
    keywords = keywords.replace(" ", "+") # replace spaces with +'s
    keywords = keywords.replace("\t", "%09") # replace tabs
    url = 'https://nominatim.openstreetmap.org/search.php?q=' + keywords + '&polygon_geojson=1&viewbox='
    html = REQUEST(url)
    # from the html look at the output and study which output is correct to get the internal data from the search
    return html