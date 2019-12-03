import urllib2
import socket # needed for timeout

def writefile(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()


def readfile(filename):
    file = open(filename, "r")
    return file.read()


def internet_on(address):
    for timeout in [1,5,10,15]:
        try:
            response=urllib2.urlopen(address,timeout=timeout)
            return True
        except urllib2.URLError as err: pass
    print "INTERNET OFFLINE"
    return False

def file(directory, filename, html, type):
    import os.path
    #directory = './html/'
    #filename = "file.html"
    filename = filename.replace('/','_')
    filename = filename.replace('~', '-')
    filename = filename + ".html"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory) # make a new directory
    if type == "write":
        file = open(file_path, type)
        file.write(html)
        file.close()
    elif type == "read" and os.path.exists(file_path): # read the old file
        file = open(file_path, type)
        html = file.read()
        file.close()
    else:
        return None
    return html


def REQUEST(address):
    #if internet_on(address):
    timeout = 60
    socket.setdefaulttimeout(timeout)
    user_agent = 'VLA. + RESEARCH SCIENCE (Linux/MacOS; West Coast, USA)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url=address, headers=headers)
    #address = "http://ashercmartin.wordpress.com/links/"
    #filename = address.split("?")[0].split("/")[-1]
    html = file("./html/", address, "", "read")
    if html is None:
        response = urllib2.urlopen(req)
        html = response.read()
        file("./html/", address, html, "write")
        print " REQUEST (ONLINE): " + address
    else:
        print "REQUEST (OFFLINE): " + address
    import nlp
    nlp.frequency(html)

    # todo: add some code later if the request fails to still save a file
    return html
    #else:
    #    print "WARNING: CONNECTION OFFLINE READING LOCAL FILE"
    #    return readfile("file.html")