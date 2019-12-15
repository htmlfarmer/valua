import xml.etree.ElementTree as ET
from request import FILE_REQUEST

def cia(website):
    website.path = "./cia_fact_book/"
    website.html = FILE_REQUEST(website.url, website.path)
    website.xml = ET.fromstring(website.html)
    return

def cia_indexer(website):
    website.path = "./cia_fact_book/"
    website.html = FILE_REQUEST(website.url, website.path)
    website.xml = ET.fromstring(website.html)
    root = website.xml
    xpath = './/*[@id="search-place"]'
    root.find(xpath)
    return
