import requests

import json

node = 'http://153.122.13.96:7890' #japan server　必要に応じてサーバーを変更してください

api = '/account/transfers/outgoing'

parameter = 'address=ネムログのアドレスをいれてください'　#nemlog

url = str(node + api + '?' + parameter)

r = requests.get(url).json()

#wright to file

wf = open('outgoing.json','w')

json.dump(r,wf,indent=4)
