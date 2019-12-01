
import xml.etree.ElementTree as ET
from request import GET_REQUEST

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
    html = GET_REQUEST(url)
    # study the doccument for the search results
    root = ET.fromstring(html)
    # xpath to look for //*[@id="mw-content-text"]/div[3]/ul/li[1]/div[1]/a
    index = './/*[@id="mw-content-text"]/div[3]/ul/li[1]/div[' + str(1) + ']/a'
    search_result = root.find(index)
    # xpath of the first search term //*[@id="mw-content-text"]/div[3]/ul/li[1]/div[1]/a/span[1]
    # xpath of "ALL" the search results looks like this //*[@id="mw-content-text"]
    # xpath of the second result //*[@id="mw-content-text"]/div[3]/ul/li[2]/div[1]/a
    # xpath of the third  result //*[@id="mw-content-text"]/div[3]/ul/li[3]/div[1]/a/span
    # xpath of the first  result //*[@id="mw-content-text"]/div[3]/ul/li[4]/div[1]/a
    if search_result is None:
        print name + " no further search xpath search test correct page!"
    else:
        website = "https://en.wikipedia.org" + search_result.attrib["href"]
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

def wiki_stock(html):

    # doccumentation on elementtree
    # https://docs.python.org/2/library/xml.etree.elementtree.html
    root = ET.fromstring(html)
    revenue_increase = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[16]/td/span')._children[0].tail
    operating_income = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[17]/td/span').text
    net_income = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[18]/td/span').text
    total_assets = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[19]/td/span').text
    total_equity = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[20]/td/span').text
    #owner = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[21]/td/span').text
    #employees = root.find('.//*[@id="mw-content-text"]/div/table[1]/tbody/tr[22]/td/span').text

    print "revenue_increase = " + revenue_increase
    print "operating_income = " + operating_income
    print "net_income = " + net_income
    print "total_assets = " + total_assets
    print "total_equity = " + total_equity
    #print "owner = " + owner
    #print "employees = " + employees
