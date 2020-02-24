import json
import requests
import sys

args = sys.argv


node = 'http://153.122.13.96:7890'
api = '/namespace?namespace='
namespace = args[1]

url = str(node + api + namespace )

print(url)
r = requests.get(url).json()

print(json.dumps(r,indent=4))


