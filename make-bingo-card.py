import json
import sys
import random
 
with open('guildadd.json', 'r') as f:
        data = json.load(f)
        print(data)
        data2 = data['data']
        print(data2)
 
        for n in range(1,7):
                str1 = '{}'.format(data2[n-1]['address'])
                name1 = '{}'.format(data2[n-1]['name'])
                m = str(n).zfill(4)
                f = list(range(1,10))
                g = random.sample(f,5)
                message = ("card_no: ",m,"your_no: ",g)
 
#                print("address:",str1)
                print("name:",name1)
                print("card_no:",m)
                print("your_no",g)
