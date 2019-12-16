import time
import urllib.request
from urllib.request import urlopen
import re
import http.cookiejar, urllib.request
from http.cookiejar import CookieJar
import datetime

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://www.huffingtonpost.com/feeds/index.xml'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'',sourceCode)
            links = re.findall(r'(.*?)',sourceCode)
            for title in titles:
                print (title)
            for link in links:
                print (link)
        except Exception as e:
            print (e)

    except Exception as e:
        print (e)
        pass

"""
main()
"""
		
