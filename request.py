import urllib.request

# HTTP REQUEST of some address
def REQUEST(address):
    req = urllib.request.Request(address)
    req.add_header('User-Agent', 'VALUA. + NLP RESEARCH / SCIENCE (Linux/MacOS; Pacific North West Coast, USA)')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')  # make sure its all text not binary
    print("REQUEST (ONLINE): " + address)
    return html


def WRITEFILE(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()


# read in a file and print it and process the data
def READFILE(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()  # preprocess line
            #print (line)
            lines.append(line)  # storing everything in memory!
    return lines

import os.path
def FILE_IO(file):
    # local variables from {dictionary}
    directory = file["directory"]
    filename = file["filename"]
    text = file["data"]
    type = file["type"]
    # correct any filename problems
    filename = filename[filename.rfind("/")+1:]
    filename = filename.replace('/','_')
    filename = filename + ".html"
    file_path = os.path.join(directory, filename)
    # check to see if the directory exists
    if not os.path.isdir(directory):
        os.mkdir(directory) # make a new directory
    if type == "write":
        file = open(file_path, "w") # for python 2.7 you need the full word "write"?
        file.write(text)
        file.close()
    elif type == "read" and os.path.exists(file_path): # read the old file
        file = open(file_path, "r") # for python 2.7 you need the full word "read"?
        text = file.read()
        file.close()
    else:
        return None
    return text


# check to see if the file exists if it does return the html from the file
# if not write a new file and return the html
def FILE_REQUEST(address, directory):
    html = READ_FILE_REQUEST(address, directory)
    if html is None:
        html = WRITE_FILE_REQUEST(address, directory)
    return html

# read a http request from a directory
def READ_FILE_REQUEST(address, directory):
    filename = address
    data = {"directory": directory,
            "filename": filename,
            "data" : "",
            "type": "read"}
    html = FILE_IO(data)
    if html is None:
        print("WARNING NO LOCAL COPY OF WEBSITE: " + filename)
    return html


# save a http request to a directory
def WRITE_FILE_REQUEST(address, directory):
    html = REQUEST(address)
    data = {"directory": directory,
            "filename": address,
            "data": html,
            "type": "write"}
    FILE_IO(data)
    return html
