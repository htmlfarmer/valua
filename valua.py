# by Asher Martin
# November 2019
# About: this program is designed to help search for news and evaluate it.

from website import Website
import datetime
import wikipedia
from file import READ

websites = []


#############################################
#          MAIN PROGRAM OUTLINE
#############################################
# the main goal of this program is to take in a user input and then search all the cities on earth
# and find the geo locations and city names of the most likely areas

URL_CITY_ARRAY = [
    'https://en.wikipedia.org/wiki/Moscow,_Idaho', \
    'https://en.wikipedia.org/wiki/Seattle', \
    'https://en.wikipedia.org/wiki/Singapore', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_A', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_B', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_C', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_D', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_E', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_F', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_G', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_H', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_I', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_J', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_K', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_L', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_M', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_N', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_O', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_P', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_Q', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_R', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_S', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_T', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_U', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_V', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_W', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_X', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_Y', \
    'https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_Z']

CIA_FACT_BOOK = ['https://www.cia.gov/library/publications/the-world-factbook/geos/us.html']

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

def main_country():
    """
    cities = []
    fact_book = []
    #for country in CIA_FACT_BOOK:
    #    CIA.cia_indexer(Website(country))
    for city in URL_CITY_ARRAY:
        cities.append(Website(city))
    for city in cities:
        wikipedia.wiki_study_city(city)
    """
    return

def main():

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

    # READ IN ALL SP500 and NASDAQ INFO
    nasdaq = READ("nasdaq.txt", ".")
    sp100 = READ("sp500.txt")

    for stock in nasdaq.splitlines():
        print("NASDAQ SEARCH: " + stock)
        url = wikipedia.wiki_search(stock)
        webpage = Website(url)
        webpage.set_directory("./wikipedia/")
        html = webpage.get_html()
        xml = webpage.get_xml()
        websites.append(webpage)

    for stock in sp100.splitlines():
        print ("EVALUATING STOCK SP500 " + stock)
        wikipedia.wiki_search(stock)




# http://ec.europa.eu/eurostat/web/json-and-unicode-web-services/getting-started/rest-request
# DATABASE: http://ec.europa.eu/eurostat/data/database


print("===================================================")
print("  REPORT # " + str(datetime.datetime.now()))
print("    DATE : " + str(datetime.date.today().strftime("%B")) + " " \
      + str(datetime.date.today().strftime("%d")) + ", " \
      + str(datetime.date.today().strftime("%Y")))
print("===================================================")

from request import REQUEST

"""
# Do a Wikipedia Lookup Based on geolocation (Cape Cod, MA) http://api.geonames.org/findNearbyWikipedia?lat=41.618116&lng=-70.485361&username=demo
wikihtml = GET_REQUEST("http://api.geonames.org/findNearbyWikipedia?lat="+ str(lat) +"&lng="+ str(lng) + "&username=asolr")
wiki = ET.fromstring(wikihtml) # if you need the xml data type
print ET.tostring(wiki)
"""

# TODO: request API + https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module



main()
