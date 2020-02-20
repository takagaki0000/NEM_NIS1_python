import requests

import json

import os

import random

 

node  = random.choice(("http://alice2.nem.ninja:7890",\

"http://alice3.nem.ninja:7890","http://alice4.nem.ninja:7890",\

"http://alice5.nem.ninja:7890","http://alice6.nem.ninja:7890",\

"http://alice7.nem.ninja:7890"));

api = '/account/transfers/incoming'

 

parameter = 'address=調べたいアドレスをここに代入'

url = str(node + api + '?' + parameter)

 

r = requests.get(url).json()

 

data2 = r['data']

 

# １から２５まで　繰り返して表示

#id　message の表示

 

for n in range(1,25):

 

        print(n)

        print('id:{}'.format(data2[n]['meta']['id']))  #idの表示

        print('message:{}'.format(data2[n]['transaction']['message']))　 #messageの表示


