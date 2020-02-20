import json
import requests

node  = random.choice(("http://alice2.nem.ninja:7890",\
"http://alice3.nem.ninja:7890","http://alice4.nem.ninja:7890",\
"http://alice5.nem.ninja:7890","http://alice6.nem.ninja:7890",\
"http://alice7.nem.ninja:7890"));
api = '/account/mosaic/owned'
parameter = 'address=知りたいアドレス' 
url = str(node + api + '?' + parameter )

print(url)
r = requests.get(url).json()
print(json.dumps(r,indent=4))

p = r['data']

print(json.dumps(p,indent=4)) 

max = len(p)

print('max =',max)

for n in range(0,max):
        mosaic_data = 'mosaicid:{}'.format(p[n]['mosaicId']['namespaceId'])
        mosaic_name = 'mosaicid:{}'.format(p[n]['mosaicId']['name'])
        number = 'number:{}'.format(p[n]['quantity'])
        print('no.',n)
        print('mosaic_data',mosaic_data)
        print('mosaic_name',mosaic_name)
        print('number',number)

