#!/usr/bin/env python3

from requests import get, RequestException
from bs4 import BeautifulSoup as bs
from contextlib import closing
from sys import argv
from re import match, IGNORECASE


if len(argv) != 2:
    print(argv[0] + ' takes exactly one argument, a url')
    exit(1)

url = argv[1]

body = None
try:
    with closing(get(url, stream=True)) as resp:
        if match('.*html.*',
                 resp.headers['Content-Type'],
                 flags=IGNORECASE):
            body = resp.content
        else:
            print('non-html content type: ' + str(resp.headers))
            exit(1)
except RequestException as ee:
    print('Error during requests to {0} : {1}'.format(url, str(ee)))

print(body)
