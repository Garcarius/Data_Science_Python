import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?' 
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ') #se inyeoduce la direccion
    if len(address) < 1: break

    parms = dict() #se crea un diccionario de parametros
    parms['address'] = address #se asigna el valor de la direccion insertadad
    print(parms['address']) #parms{"address":address} address tiene unos valores ya ingresados
    if api_key is not False: parms['key'] = api_key #es 42 por defecto
    url = serviceurl + urllib.parse.urlencode(parms) #coloca los parametros del diccionario en una linea  address=manhatan&key=42
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx) #se conecta a la direccion
    data = uh.read().decode() #se lee y decodifica
    print('Retrieved', len(data), 'characters') 

    try:
        js = json.loads(data) #method can be used to parse a valid JSON string and convert it into a Python Dictionary
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK': #en caso de que no encuentre nada , que no tenga status o status sea diferente de ok enviar el siguiente error
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
