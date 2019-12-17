import urllib.request
from file import READ
from file import WRITE


# REQUEST(address)
# DETAILS: gets the HTML from any website address


def REQUEST(address):
    req = urllib.request.Request(address)
    req.add_header('User-Agent', 'VALUA. + NLP RESEARCH / SCIENCE (Linux/MacOS; Pacific North West Coast, USA)')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')  # make sure its all text not binary
    print("REQUEST (ONLINE): " + address)
    return html


# REQUEST(address, filename, directory)
# DETAILS: gets the HTML from any website and saves it to a file and directory
# if the filename is None or "" then the address is used
# if the directory is None or "" then the default directory is "./"


def REQUEST_FILE(address, **kwargs):
    directory = kwargs["directory"]
    filename = kwargs["filename"]
    if filename is None:
        filename = address
        filename = filename.replace('/', '_')
    if directory is None:
        directory = "./"
    html = READ(filename, directory)
    if html is None:
        html = REQUEST(address)
        WRITE(filename, directory, html)
    return html
