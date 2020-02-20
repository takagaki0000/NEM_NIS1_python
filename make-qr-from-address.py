import json

import qrcode

import os

FILE_IN = 'outgoing.json'

f = open(FILE_IN, 'r')

data = json.load(f)

print('data:{}'.format(type(data)))

data2 = data['data']

# １から２５まで　繰り返して作業

#recipient(アドレス)QRコードに変換
for n in range(1,25):

 print('{}'.format(data2[n]['transaction']['recipient']))

 img = qrcode.make('{}'.format(data2[n]['transaction']['recipient']))

#img.show()

 img.save('{}'.format(data2[n]['transaction']['recipient']) + '.png')
