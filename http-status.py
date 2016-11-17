#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import urllib,sys

def main():
    parser = argparse.ArgumentParser(description="Nagios HTTP Status Check")
    parser.add_argument('url', nargs=1, help="URL to check.")
    args = parser.parse_args()

    url_to_check = args.url[0]
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
    main()
