import json
import requests
import time
import datetime
import sys
args = sys.argv

address2 = args[1]  #arg1

node = 'http://153.122.13.96:7890' 
api = '/account/namespace/page?address='
api2 = '/account/namespace/address='

url = str(node + api + address2 ) # + tail)

print(url)
r = requests.get(url).json()

print('nemlog-namespace')
print(json.dumps(r,indent=4))

#url2 = str(node + api + address1 + '&pageSize=100' )
#q = requests.get(url2).json()
#print('main-namespace')
#print(json.dumps(q,indent=4))
v=r['data']
max=len(v)
print('namespace NO')
for n in range(0,max):
	print('namespace NO',n)
	namespaceId = (v[n]['fqn'])
	print('namespaceID',v[n]['fqn'])
	print('namespace-hight',v[n]['height'])
	ht = v[n]['height']
#	print(ht)

	url3 = 'http://153.122.13.96:7890/block/at/public'
	data = {"height":ht}
	res = requests.post(url3,json=data)
	values = json.loads(res.text)
#	print(json.dumps(values,indent=4))
	data1 = values['timeStamp']
#	print('timestamp = ',data1)
	dt1 = datetime.datetime.fromtimestamp(data1+1425135985)
	print('timestamp = ',data1+1425135985)
	dt2 = datetime.datetime.fromtimestamp(data1+1425135985+31592080)

	print('namespace made in ',dt1)
	print('namespace Expired at ',dt2)
	print('!')
	print('nextdata')
	print('!!')
time.sleep(1)

#url4 = str(node + api + address1 +'&id=200000' )
#p = requests.get(url3).json()
#print('main-namespace')
#print(json.dumps(p,indent=4))
