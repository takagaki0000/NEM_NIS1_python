import requests

import json

 

FILE_IN = 'incoming.json'

 

f = open(FILE_IN, 'r')

 

data = json.load(f)

 

#print('data:{}'.format(type(data)))

 

data2 = data['data']

 

# １から２５まで　繰り返して表示

 

#id　timestamp recipient の表示

 

for n in range(1,25):

 

# print('id:{}'.format(data2[n]['meta']['id']))

 

# print('timeStamp:{}'.format(data2[n]['transaction']['timeStamp']))

 

 print('signer:{}'.format(data2[n]['transaction']['signer'])) #signer

 

 pkey = ('{}'.format(data2[n]['transaction']['signer']))

 

# print('pkey' + pkey)

 

 node = 'http://153.122.13.96:7890' #japan server

 api = '/account/get/from-public-key?'

 

 parameter = 'publicKey='+ str(pkey)

# print('parameter: '+parameter)

 

 url = str(node + api + parameter)

 

# print('url: ' + url)

 

 r = requests.get(url).json()

 print('address: {}'.format(r['account']['address']))

#print(json.dumps(r,indent=4))

 
