import xml.etree.ElementTree as ET
from request import REQUEST


# this part of the program will be valuable to study
# List of towns and cities with 100,000 or more inhabitants
def wiki_cities():
    # first load all the cities from A to Z into a file
    # read in each city
    # read in the coordinates for the city
    # save the name of the city and country to the file

    URL_CITY_ARRAY = [
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
    for city in URL_CITY_ARRAY:
        html = REQUEST(city)
    root = ET.fromstring(html)

    return


def wiki_location_estimate():
    return


# source: https://stackoverflow.com/questions/54516687/how-to-print-get-specific-lines-in-an-html-file-in-python-3
# https://stackoverflow.com/questions/11709079/parsing-html-using-python

# load a search from wikipedia and then pick the correct page from the search
# EXAMPLE SEARCH URL:
# https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=APPLE+INC.%09AAPL&title=Special%3ASearch&go=Go&ns0=1
# parsed URL:
# https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=                 &title=Special%3ASearch&go=Go&ns0=1


from difflib import SequenceMatcher


# https://docs.python.org/2/library/difflib.html
def similar(a, b):
    # similarity = SequenceMatcher(None, a, b).ratio()
    a = a.lower()
    b = b.lower()
    similarity = SequenceMatcher(lambda x: x in " \t", a, b)
    s = round(similarity.ratio(), 3)
    print "SequenceMatcher: (" + a + ") : (" + b + ") ratio = " + str(s)
    return s


def largest(arr):
    # Initialize maximum element
    max = arr[0]
    n = len(arr)
    # Traverse array elements from second
    # and compare every element with
    # current max
    for index in range(1, n):
        if arr[index] > max:
            max = arr[i]

    return index


# find which of the returned links can be used
def wiki_study_search(keywords, root):
    xpath = './/*[@id="mw-content-text"]/div[3]/ul/li[1]/div[' + str(1) + ']/a'
    # did the search result have good data or not
    if root.find(xpath) is None:  # this means that a search was NOT successful
        print "XPATH ERROR! Search Result Failed.  check to see if there was a search result?"
        return None
    else:  # grab the search result and go to that website to read the stock market info
        similarity = []
        for i in range(20):  # check the first 10 search results
            index = './/*[@id="mw-content-text"]/div[3]/ul/li[' + str(i + 1) + ']/div[1]/a'
            if root.find(index) is not None:  # check to see if we have a search result
                search_result = root.find(index).attrib[
                    "title"]  # //*[@id="mw-content-text"]/div[3]/ul/li[1]/div[1]/a/span
                similarity.append(similar(search_result, keywords))
            else:
                break  # break from the loop
        maxindex = similarity.index(max(similarity))
        # now go to the similarity index and pick that one to forward and get the href http address
        index = './/*[@id="mw-content-text"]/div[3]/ul/li[' + str(maxindex + 1) + ']/div[1]/a'
        website_address = "https://en.wikipedia.org" + root.find(index).attrib["href"]
        return website_address


def wiki_research(keywords):
    print "WIKIPEDIA RESEARCH on: " + keywords
    # replace spaces with + and figure out what a %09 is
    search_terms = keywords.replace(" ", "+")  # replace spaces with +'s
    search_terms = search_terms.replace("\t", "%09")  # replace tabs
    # this code does the initial search and checks the search results using various links
    url = 'https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=' + search_terms + '&title=Special%3ASearch&go=Go&ns0=1'
    html = REQUEST(url)
    # study the document for the search results
    root = ET.fromstring(html)
    # get the first result of the search and test it to see if it is correct
    # the most important step is to check which of the search results have the closest match
    # check each search result and see if the title or whatever matches closely...
    website = wiki_study_search(keywords, root)
    if website is not None:
        html = REQUEST(website)
        wiki_stock(html)
    else:
        print "STOCK INFO MISSING FOR WIKIPEDIA: " + keywords  # since its an official stock page we can do a regular search
    return website


# view the news!
def wiki_news(html):
    # //*[@id="Predicted_and_scheduled"]
    # //*[@id="November"]
    root = ET.fromstring(html)
    # //*[@id="mw-content-text"]/div/ul[1] #january
    month = []
    for m in range(12):
        index = './/*[@id="mw-content-text"]/div/ul[' + str(m + 1) + ']'
        month.append(root.find(index))
    print "WIKI NEWS SAFE!"
    # read the data for each entry
    # for m in range(12):
    #    print "date: " + month[m]._children[i] + " " + month[m]


"""
Revenue	Increase US$265.595 billion[1] (2018)
Operating income
Increase US$70.898 billion[1] (2018)
Net income
Increase US$59.531 billion[1] (2018)
Total assets	Decrease US$365.725 billion[1] (2018)
Total equity	Decrease US$107.147 billion[1] (2018)
Owner	The Vanguard Group (0.0737), BlackRock (0.0676) Edit this on Wikidata
Number of employees
132,000[2] (2018)
"""


# this function gets the latitude and logitude coodrinates
# we need to add some code to do some more sophiticated search for the location
def get_location(root):
    # select the revenue index
    # select the latitude and logitude of the business or stock
    coordinates = root.find('.//*[@id="coordinates"]/span/a/span[3]/span[1]')
    if coordinates != None:
        coordinates = root.find('.//*[@id="coordinates"]/span/a/span[3]/span[1]').text
    else:
        # search for Headquarters //*[@id="mw-content-text"]/div/table[1]/tbody/tr[7]/td/text()[1]
        row = 0  # we dont know what row is the correct xpath for "Revenue" yet
        xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/td/'
        if root.find(xpath) is not None:
            for row in range(50):  # todo bad idea to hard code this think about this later
                xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/'
                if root.find(xpath).text == "Headquarters":
                    xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/td'
                    headquarters = root.find(xpath).text
                    xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/td/div[' + str(1) + ']/a'
                    if root.find(xpath) is not None:
                        headquarters = headquarters + " " + root.find(xpath).text
                    import openstreetmaps
                    coordinates = openstreetmaps.OPEN_XML_GEOCODE(headquarters)
                    break  # we found the correct row
        else:
            print "unable to find coordinates : latitude & logitude"
    return coordinates


from re import sub
from decimal import Decimal


def currencyxchange(text_money):
    if text_money is not None:
        value = Decimal(sub(r'[^\d.]', '', text_money))
        # figure out if the number was a billion
        value = float(value * 1000000000)
        return value
    else:
        return None


# this function finds the location of the financial data in wikipedia
# for detailed info on xpath xml
# https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax
def get_financial(root):
    # find the table row "tr" number then assign row
    row = 0  # we dont know what row is the correct xpath for "Revenue" yet
    xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/'
    if root.find(xpath) is not None:
        for row in range(50):  # todo bad idea to hard code this think about this later
            xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/'
            if root.find(xpath).text == "Revenue":
                break  # we found the correct row
    else:
        print "xpath not found for WIKI FINANCIALs"
        return None

    # check to see if the xpath location exists (not sure about tail)
    xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/td/span/a'
    if root.find(xpath) is not None:
        xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/td/span/a'
        revenue_increase = currencyxchange(root.find(xpath).tail)
        xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row + 1) + ']/td/span'
        operating_income = currencyxchange(root.find(xpath).text)
        xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row + 2) + ']/td/span'
        net_income = currencyxchange(root.find(xpath).text)
        xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row + 3) + ']/td/span'
        total_assets = currencyxchange(root.find(xpath).text)
        xpath = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row + 4) + ']/td/span'
        total_equity = currencyxchange(root.find(xpath).text)

        money = {"revenue_increase": revenue_increase,
                 "operating_income": operating_income,
                 "net_income": net_income,
                 "total_assets": total_assets,
                 "total_equity": total_equity}
        print "FINANICAL INFO: " + str(money)
        return money


# this function gets the financial information from each stock on wikipedia
def wiki_stock(html):
    print "WIKIPEDIA STOCK INFO FOUND!"
    # doccumentation on elementtree
    # https://docs.python.org/2/library/xml.etree.elementtree.html
    root = ET.fromstring(html)
    coordinates = get_location(root)
    print "COORDINATES (lat/lon): " + str(coordinates)
    financial = get_financial(root)
    return financial
