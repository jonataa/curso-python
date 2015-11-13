import json
import urllib.request as req
from urllib.parse import urlencode

origem = input('Origem: ')
destino = input('Destino: ')

params = urlencode({'origins': origem, 'destinations': destino, 'language': 'pt-br'})
res = req.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?%s' % params)
res_json = res.read().decode('utf-8')

data = json.loads(res_json)
for row in data['rows']:
    print (row['elements'])
    
