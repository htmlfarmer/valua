from request import GET_REQUEST

US_CENSUS_KEY = "9d4c29e072ec00a326361a8146c792f465d49186"
# https://www.census.gov/data/developers/data-sets/economic-census.html
# https://api.census.gov/data/2012/ewks/variables.html (REALLY GOOD LINK)
# EXAMPLES https://api.census.gov/data/2012/ewks/examples.html
# NAICS MANUAL: https://www.census.gov/eos/www/naics/2017NAICS/2017_NAICS_Manual.pdf
def CENSUS_ECONOMIC ():
    FIELDS = "RCPTOT,OPTAX"
    NAICS2012 = "71" # 71 ARTS AND ENTERTAINMENT
    url = "https://api.census.gov/data/2012/ewks?get=" + FIELDS + "&for=state:*&NAICS2012=" + NAICS2012 \
    + "&key=" + US_CENSUS_KEY
    text = GET_REQUEST(url)
    print text
    return text

# https://www.census.gov/data/developers/data-sets/economic-indicators.html
def CENSUS_HOUSING ():
    return

# https://www.census.gov/data/developers/data-sets/international-database.html
def CENSUS_INTERNATIONAL (location):
    return

# ACTUAL https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html
# PROJECTED https://www.census.gov/data/developers/data-sets/popest-popproj/popproj.html
def CENSUS_POPULATION ():
    population = 0
    return population

# FAQ: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html#_Toc379292359
# example: https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=4600+Silver+Hill+Rd%2C+Suitland%2C+MD+20746&benchmark=9&format=json
def CENSUS_GEOCODE (address, citystatezip):
    address = address.replace(" ", "+")
    address = address.replace(",", "%2C")
    citystatezip = citystatezip.replace(" ", "+")
    citystatezip = citystatezip.replace(",", "%2C")
    url = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=" + address + "+" + citystatezip + "&benchmark=9&format=json"
    json = GET_REQUEST(url).replace(" ", "")
    # find the logitude and latitude in the JSON reply
    start = json.find("\"x\":")
    if(start != -1):
        end = json.find(",", start)
        longitude = json[start+4:end]
        start = json.find("\"y\":")
        end = json.find("}", start)
        latitude = json[start+4:end]
    else:
        longitude = None
        latitude = None
    geocode = {"longitude" : longitude, "latitude" : latitude}
    print geocode
    return geocode

# https://www.census.gov/data/developers/data-sets/economic-indicators.html

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