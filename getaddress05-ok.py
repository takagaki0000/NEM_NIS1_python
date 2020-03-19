import json
import sys

args = sys.argv

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

 if (df2[n]['name']) == args[1]:
  print(df2[n])



