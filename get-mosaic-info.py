import json

import requests

 

node = 'http://153.122.13.96:7890' #japan server

api = '/account/mosaic/owned'

parameter = 'address=NCKW2XH4C4CL6SWCFA75GHUA5BRZH6TTOVIUPMJJ' #mozagacha

url = str(node + api + '?' + parameter )

 

print(url)

r = requests.get(url).json()

print(json.dumps(r,indent=4))

 

p = r['data']

 

#print(json.dumps(p,indent=4)) #チェック用

 

max = len(p)

 

print('max =',max)

 

for n in range(0,max):

        mosaic_data = 'mosaicid:{}'.format(p[n]['mosaicId']['namespaceId'])

        mosaic_name = 'mosaicid:{}'.format(p[n]['mosaicId']['name'])

        number = 'number:{}'.format(p[n]['quantity'])

        print('no.',n)

        print('mosaic_data',mosaic_data)

        print('mosaic_name',mosaic_name)


