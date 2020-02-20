import json

FILE_IN = 'outgoing.json'

f = open(FILE_IN, 'r')

data = json.load(f)

print('data:{}'.format(type(data)))

data2 = data['data']

# １から２５まで　繰り返して表示

#id　timestamp recipient の表示

for n in range(1,25):

 print('id:{}'.format(data2[n]['meta']['id']))

 print('timeStamp:{}'.format(data2[n]['transaction']['timeStamp']))

 print('recipient:{}'.format(data2[n]['transaction']['recipient']))
