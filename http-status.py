import urllib,sys

url_to_check = sys.argv[1]
status = ""

def http_status():
    a = urllib.urlopen(url_to_check)
    return a.getcode()
def soap_check():
    stuff

try:
    if http_status() == 200:
        status = "status 200"
        exit = 0
    else:
        status = "URL returned %s" % http_status()
        exit = 1
except:
    print 'Unkown error - Can\'t connect to %s' % url_to_check
    sys.exit(1)

print status
print exit
