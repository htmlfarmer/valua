import urllib2
import socket # needed for timeout


def writefile(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()


def REQUEST(address):
    timeout = 60
    socket.setdefaulttimeout(timeout)
    user_agent = 'VALUA. + RESEARCH SCIENCE (Linux/MacOS; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url = address, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    writefile("file.html", html) #save a local copy
    #todo add some code later if the request fails to still save a file
    return html