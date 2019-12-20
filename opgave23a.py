#!/usr/bin/env python3
import sys
import re
import urllib.request
# verify number of arguments
#

if len(sys.argv) != 2:
    sys.exit('Usage: %s <URL>' % sys.argv[0])

url = sys.argv[1]

# add prefix if needed
#
if not url.startswith("http://"):
    url = "http://" + url
# open URL
#
try:
    web = urllib.request.urlopen(url)
except Exception as e:
    sys.exit('Open URL: %s' % e)

# read entire webpage as bytes object
#
contents = web.read()
encoding = 'utf−8' # take utf−8 as default
# convert entire webpage to string
#
contents = contents.decode(encoding)
# compile RE and find all occurences of ’<img ’
#
zoeker = re.compile("<IMG ", re.IGNORECASE)
images = zoeker.findall(contents)
print('Webpagina %s bevat %d plaatjes (%s)' % (web.geturl(), len(images), encoding))
