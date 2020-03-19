import json
import sys

args = sys.argv

print("address = ",args[1] )

with open('./nemlog03-ok.json') as f:

# print(f.read())

 df = json.load(f)
 df2 = df['data']

 print(type(df2))
# print(df2)

# print(df2['えっさん'])

# print(format(df2[1]))

max = len(df2)

for n in range(0,max):

 if (df2[n]['address']) == args[1]:
  print(df2[n])

#res = []
#for v in df2:
#    if isinstance(v, str):
#        res.append(v)
        
#print(res) # ["a", "b"]

#res = []
#for arg in df2:
#    if isinstance(arg, str):
#        res.append(arg)
#    if isinstance(arg, list):
#        for v in arg:
#            if isinstance(v, str):
#                res.append(v)

#print(res) # ["a", "b"]

