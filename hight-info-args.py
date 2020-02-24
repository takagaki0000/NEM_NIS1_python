import requests
import json
import datetime
import sys

args = sys.argv

url = 'http://153.122.13.96:7890/block/at/public'
data = {"height":args[1]}
res = requests.post(url,json=data)
values = json.loads(res.text)

#print(values)
#print(json.dumps(values,indent=4))

#time = ['timeStamp']
data1 = values['timeStamp']

dt = datetime.datetime.fromtimestamp(data1+1425135985)
print(data1)
print(dt)

#date1 = datetime.datetime.fromtimestamp((2015, 2, 29, 0, 6, 25, 0) + (data1 * 1000))
#print(date1)
#print(time)
#print('main-timesatmp',time)
