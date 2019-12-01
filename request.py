import urllib2
import socket # needed for timeout

def GET_REQUEST(address):
    timeout = 60
    socket.setdefaulttimeout(timeout)
    user_agent = 'VALUA. + RESEARCH SCIENCE (Linux/MacOS; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url = address, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html