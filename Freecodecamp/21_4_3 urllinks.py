# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context() #This example creates a SSL context with the recommended security settings for client sockets, including automatic certificate verification
ctx.check_hostname = False  #turn-off hostname verification
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() 
#lee la url con el certificado de seguridad anterior, pero lee la pagina en su totalidad
soup = BeautifulSoup(html, 'html.parser') 
#analizer of html

# Retrieve all of the anchor tags
tags = soup('a') #<a /a> anchor tag
for tag in tags:
    print(tag.get('href', None)) #<a href="https://..."  /a>