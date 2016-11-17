import urllib,sys

def __main__():

    url_to_check = sys.argv[1]
    status = ""

    try:
        url_check = urllib.urlopen(url_to_check)
        url_status = url_check.getcode()
        if url_status == 200:
            status = "Status 200"
            exit = 0
        else:
            status = "URL returned %s" % url_status
            exit = 1
    except:
        print "Unknown error - Can\'t connect to %s" % url_to_check
        exit = 1
        sys.exit()
    print status
    print exit

if __name__ == "__main__":
    __main__()
