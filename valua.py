import urllib
import urllib2
import socket # needed for timeout
import re
import xml.etree.ElementTree as ET

# TODO: request API + https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module

#harmonic mean
#from scipy import stats
#import numpy

test = '<tr ng-repeat="measure in component.measures" class="measure ng-scope" style="">\
            <!-- ngIf: measure.showDetails != 1 -->\
            <!-- ngIf: measure.showDetails == 1 --><td ng-if="measure.showDetails == 1" \
            class="name measure-name ng-scope" title="Percentage of adults reporting fair \
            or poor health (age-adjusted)"> \
                <a ui-sref="measures.state.tab({ category: categoryId == 1 ? \'outcomes\' \
                : \'factors\', measure: measure.id, tab: \'map\' })" \
                href="/app/california/2017/measure/outcomes/2/map"> \
                  <span ng-bind-html="measure.name" class="ng-binding">Poor or fair health</span> \
                  <!-- ngIf: snapshot_printing -->\
                </a>\
            </td><!-- end ngIf: measure.showDetails == 1 -->\
            <!-- ngIf: !snapshot_printing --><td ng-if="!snapshot_printing" \
            class="info noPrint popover--wide ng-scope"><!-- ngIf: measure.hasFootnote -->\
            <span class="fa fa-info-circle ng-scope" ng-if="measure.hasFootnote" \
            data-bs-popover="footnotePopover" data-placement="bottom" data-trigger="click" \
            data-container="body" data-content="Data should not be compared with prior years" \
            data-html="true"><span>(Click for info)</span></span><!-- end ngIf: measure.hasFootnote -->\
              <!-- ngIf: measure.id === 1 && cdcData.length --></td><!-- end ngIf: !snapshot_printing -->\
            <td class="value" ng-class="{\'highlight\': measure.area_to_highlight != 0, \'highlight-explore\': \
            measure.area_to_highlight == 2, \'highlight-strength\': measure.area_to_highlight == 1}"> \
                <!-- ngIf: measure.area_to_highlight == 2 -->\
                <!-- ngIf: measure.area_to_highlight != 2 -->\
                <span ng-if="measure.area_to_highlight != 2" ng-bind-html="measure.displayValue" \
                class="ng-binding ng-scope">12%</span><!-- end ngIf: measure.area_to_highlight != 2 -->\
            </td>\
            <!-- Trend -->\
            <!-- ngIf: isDefaultYear --><td ng-if="isDefaultYear" class="trend-icon-value mobile-drop ng-scope">\
                <!-- ngIf: measure.trend -->\
            </td><!-- end ngIf: isDefaultYear -->\
            <!-- Error margin -->\
            <td class="error-margin mobile-drop ng-binding" ng-bind-html="measure.displayCIRange">11-12%</td>\
            <!-- National benchmark -->\
            <td class="target mobile-drop ng-binding" ng-bind-html="measure.displayTarget">12%</td>\
            <!-- State value -->\
            <!-- ngIf: current.state_fips != \'11\' -->\
            <td ng-if="current.state_fips != \'11\'" \
            class="state-value ng-binding ng-scope" \
            ng-bind-html="measure.displayState">18%</td>\
            <!-- end ngIf: current.state_fips != \'11\' -->\
            <!-- Measure row does not show a value for Rank. -->\
            <!-- ngIf: current.state_fips != \'11\' -->\
            <td ng-if="current.state_fips != \'11\'" \
            class="rank ng-scope">&nbsp;</td><!-- end ngIf: current.state_fips != \'11\' --></tr>'

ZILLOW_KEY = "X1-ZWz18uigx8hcej_1acr8"

# goal is to compare yelp with ZILLOW
def MAIN ():
    """
    locations = [{"address" : "412 6th Ave", "citystatezip" : "Tacoma, WA 98402"},
        {"address" : "2028 S 7th St", "citystatezip" : "Tacoma, WA 98405"}, \
        {"address" : "708 S Junett St", "citystatezip" : "Tacoma, WA 98405"}, \
        {"address" : "1111 Morse Ave SPC 168", "citystatezip" : "Sunnyvale, CA 94089"}, \
        {"address" : "251 N 19TH St", "citystatezip" : "San Jose, CA 95112"}, \
        {"address" : "252 Sonora Pass Rd", "citystatezip" : "Vallejo, CA 94589"}, \
        {"address" : "628 2nd St", "citystatezip" : "Rodeo, CA 94572"}, \
        {"address" : "339 W Chanslor Ave", "citystatezip" : "Richmond, CA 94801"}, \
        {"address" : "1468 Sandpiper Spit", "citystatezip" : "Richmond, CA 94801"}, \
        {"address" : "0 Treasure Island Dr", "citystatezip" : "Aptos, CA 95003"}, \
        {"address" : "834 Loma Prieta Dr", "citystatezip" : "Aptos, CA 95003"}, \
        {"address" : "321 N Howard St.", "citystatezip" : "Moscow, ID"}, \
        {"address" : "210 E 1st Street", "citystatezip" : "Moscow, ID"}]
    """
    locations = [{"address" : "2923 71st Street", "citystatezip" : "Woodridge, IL 60517"},
                 {"address" : "321 N Howard St.", "citystatezip" : "Moscow, ID"},
                 {"address" : "210 E 1st Street", "citystatezip" : "Moscow, ID"}]
        
    for location in locations :
        #print location
        #html = ZILLOW(location["address"], location["citystatezip"])
        #PARSE_ZILLOW_XML(html)
        location = CENSUS_GEOCODE(location["address"], location["citystatezip"])

def CDC_HEALTH_PARSE(html):
    start = html.find("Poor or fair health")
    if start != -1:
        end = html.find("%", start)
        data = html[end-2:end]
    if data != -1:
        print data
        return int(data)
    else:
        return None

def CDC_HEALTH(state, county):
    url = "http://www.countyhealthrankings.org/app/" + state + "/2017/rankings/" + county + "/county/outcomes/overall/snapshot"
    html = GET_REQUEST(url)
    CDC_HEALTH_PARSE(html)
    return html

def DISPLAY(html): #experimental doesn't work yet
    print re.sub("<.*?>", "", html)

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

def PARSE_ZILLOW_XML(text):
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

def VALUA (house):
    print "VALUA.ORG"
    # 1.) COMPARISON
    print "1.) COMPARISON"
    print "2.) COST (NEW)"
    print "3.) INCOME (RENTAL)"
    return

def VALUA_RADAR(address, latitude, longitude):
    # function collects all the data needed on a particular address or lat/lng
    return

def VALUA_TITLE (address, latitude, longitude):
    print "PROPERTY TITLE EVALUATION: https://en.wikipedia.org/wiki/Title_(property)"
    return

def VALUA_LOAN (address, latitude, longitude):
    # BARROWERS
    # LENDERS
    # MONTHLY PAYMENT
    print "PROPERTY LOAN EVALUATION: https://en.wikipedia.org/wiki/Mortgage_loan"

# FAQ: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html#_Toc379292359
# example: https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=4600+Silver+Hill+Rd%2C+Suitland%2C+MD+20746&benchmark=9&format=json
def CENSUS_GEOCODE (address, citystatezip):
    address = address.replace(" ", "+")
    address = address.replace(",", "%2C")
    citystatezip = citystatezip.replace(" ", "+")
    citystatezip = citystatezip.replace(",", "%2C")
    url = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=" + address + "+" + citystatezip + "&benchmark=9&format=json"
    json = GET_REQUEST(url).replace(" ", "")
    start = json.find("\"x\":")
    end = json.find(",", start)
    longitude = json[start+4:end]
    start = json.find("\"y\":")
    end = json.find("}", start)
    latitude = json[start+4:end]
    return {"longitude" : longitude, "latitude" : latitude}

# https://www.census.gov/data/developers/data-sets/economic-indicators.html
def CENSUS_HOUSING ():
    return

# https://www.census.gov/data/developers/data-sets/Health-Insurance-Statistics.html
# https://www.census.gov/geographies/reference-files/2016/demo/popest/2016-fips.html
def CENSUS_HEALTH():
    # SAN JOSE:
    # BERKELY:
    # OAKLAND:
    # VALEJO: 
    # SAN MATAO: 
    # CHICAGO: 
    # MOSCOW: 
    # NEW YORK:
    # BROOKLYN:
    # QUEENS:
    # BRONX:
    # SEATTLE:
    # PORTLAND: 
    return

def GET_REQUEST(address):
    timeout = 60
    socket.setdefaulttimeout(timeout)
    user_agent = 'VALUA. + RESEARCH SCIENCE (Linux; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url = address, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

MAIN()
