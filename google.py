from request import REQUEST

GOOGLE_API_KEY = "AIzaSyAD3AiNwlR6x-rHjYGbp277Whqf3t6LKvQ"

def GOOGLE_PLACES_DETAILS(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + place_id + "&key=" + GOOGLE_API_KEY
    json = REQUEST(url)
    return json

# EXAMPLE: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
def GOOGLE_GEOCODE(address):
    address = address.replace(" ", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + GOOGLE_API_KEY
    json = REQUEST(url)
    start = json.find("\"location\" : ")
    if(start != -1):
        start = json.find("\"lat\" : ", start)
        end = json.find(",", start)
        latitude = json[start+8:end].replace('\n', '').replace(' ', '')
        start = json.find("\"lng\" : ")
        end = json.find("}", start)
        longitude = json[start+8:end].replace('\n', '').replace(' ', '')
    else:
        longitude = None
        latitude = None
    geocode = {"longitude" : longitude, "latitude" : latitude} 
    return geocode

def GOOGLE_PLACES_ID(json):
    ids = []
    start = json.find("\"places_id\" : ")
    while start != -1:
        end = json.find(",", start)
        place_id = json[start+14:end]
        ids = ids.append(place_id)
        start = json.find("\"places_id\" : ", end) # start = last end
    print ids
    return ids

def GOOGLE_PLACES_RATINGS(json):
    ratings = []
    start = json.find("\"rating\" : ")
    while start != -1:
        end = json.find(",", start)
        rating = json[start+11:end]
        ratings.append(float(rating))
        start = json.find("\"rating\" : ", end) # start = last end
    print ratings
    return ratings

def GOOGLE_PLACE_TYPES(json):
    types = ""
    start = json.find("\"types\" : [")
    while start != -1:
        end = json.find("],", start)
        typed = json[start+11:end]
        types = types + typed + ","
        start = json.find("\"types\" : ", end) # start = last end
    print types[0:len(types)-1].replace('\n', '').replace(' ', '')
    return types[0:len(types)-1].replace('\n', '').replace(' ', '')

# GOOGLE PLACES API https://developers.google.com/places/web-service/
# https://maps.googleapis.com/maps/api/place/textsearch/json?query=123+main+street&key=YOUR_API_KEY
def GOOGLE_PLACES(location):
    if location["latitude"] != None and location["longitude"] != None:
        radius = "5000"
        #types = "food"
        # &keyword=vegetarian
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" \
        + location["latitude"] + "," + location["longitude"] + "&radius=" + radius + "&name=" \
        + "&sensor=false&key=" + GOOGLE_API_KEY
        json = REQUEST(url)
        GOOGLE_PLACES_RATINGS(json)
        GOOGLE_PLACE_TYPES(json)
        print json
        return json
    else:
        return None
