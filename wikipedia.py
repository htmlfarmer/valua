
import xml.etree.ElementTree as ET
from request import REQUEST

# source: https://stackoverflow.com/questions/54516687/how-to-print-get-specific-lines-in-an-html-file-in-python-3
# https://stackoverflow.com/questions/11709079/parsing-html-using-python

# load a search from wikipedia and then pick the correct page from the search
# EXAMPLE SEARCH URL:
# https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=APPLE+INC.%09AAPL&title=Special%3ASearch&go=Go&ns0=1
# parsed URL:
# https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=                 &title=Special%3ASearch&go=Go&ns0=1


def wiki_research(keywords):
    # replace spaces with + and figure out what a %09 is
    name = keywords
    keywords = keywords.replace(" ", "+") # replace spaces with +'s
    keywords = keywords.replace("\t", "%09") # replace tabs
    url = 'https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&search=' + keywords + '&title=Special%3ASearch&go=Go&ns0=1'
    html = REQUEST(url)
    # study the doccument for the search results
    root = ET.fromstring(html)
    # get the first result of the search and test it to see if it is correct
    index = './/*[@id="mw-content-text"]/div[3]/ul/li[1]/div[' + str(1) + ']/a'
    search_result = root.find(index)
    # did the search result have good data or not
    if search_result is None: # this means that a search was successful
        print name + " no further search xpath search test correct page!"
    else: # grab the search result and go to that website to read the stock market info
        website = "https://en.wikipedia.org" + search_result.attrib["href"]
        html = REQUEST(website)
        wiki_stock(html) # since its an official stock page we can do a regular search
        return website

# view the news!
def wiki_news(html):
    # //*[@id="Predicted_and_scheduled"]
    # //*[@id="November"]
    root = ET.fromstring(html)
    # //*[@id="mw-content-text"]/div/ul[1] #january
    month = []
    for m in range(12):
        index = './/*[@id="mw-content-text"]/div/ul[' + str(m+1) + ']'
        month.append(root.find(index))
    print "WIKI NEWS SAFE!"
    # read the data for each entry
    #for m in range(12):
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


# this function gets the financial information from each stock on wikipedia
def wiki_stock(html):

    # doccumentation on elementtree
    # https://docs.python.org/2/library/xml.etree.elementtree.html
    root = ET.fromstring(html)

    # select the revenue index
    # select the latitude and logitude of the business or stock
    coordinates = root.find('.//*[@id="coordinates"]/span/a/span[3]/span[1]')
    if coordinates != None:
        coordinates = root.find('.//*[@id="coordinates"]/span/a/span[3]/span[1]').text

    # find the table row "tr" number then assign row
    rw = 0
    for row in range(100):
        index = './/*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(row) + ']/'
        if root.find(index).text == "Revenue":
            rw = row
            break

    # check to see if the location exists (not sure about tail)
    if root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(rw) + ']/td/span/a') is not None:
        revenue_increase = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(rw) + ']/td/span/a').tail
        operating_income = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(rw+1) + ']/td/span').text
        net_income = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(rw+2) + ']/td/span').text
        total_assets = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(rw+3) + ']/td/span').text
        total_equity = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[' + str(rw+4) + ']/td/span').text

        print "revenue_increase = " + revenue_increase
        print "operating_income = " + operating_income
        print "net_income = " + net_income
        print "total_assets = " + total_assets
        print "total_equity = " + total_equity