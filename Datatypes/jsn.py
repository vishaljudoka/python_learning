import json
from urllib.request import urlopen

from Datatypes.need import p
from Datatypes.py_cls.yahoo_wapi import Wapi


w1 = Wapi()
#result=w1.get_yahoo_weather("buenos aires")

def dft():
  w1 = Wapi()
  result=w1.get_yahoo_weather("buenos aires")
  for key in result :
    #print( type(result[key]),key, ':', result[key])
    if type(result[key]) is dict:
      for i in  result[key]:
        if type(result[key][i]) is dict:
          p()
          for j in result[key][i]:
            print( j, ':', result[key][i][j])
        elif type(result[key][i]) is list:
          print("List again")
        else:
          print(i, ':', result[key][i])


    elif type(result[key]) is list:
      p()
      for lst in result[key]:
        if type(lst) is dict:
          p()
          for i in lst:
            print( i , ":" , lst[i])
        else:
          print(lst)


    else:
      print("Error")




"""
location : {'city': 'Delhi', 'region': ' DL', 'woeid': 2295019, 'country': 'India', 'lat': 28.643999, 'long': 77.091003, 'timezone_id': 'Asia/Kolkata'}
current_observation : {'wind': {'chill': 90, 'direction': 135, 'speed': 8.08}, 'atmosphere': {'humidity': 60, 'visibility': 10.0, 'pressure': 28.85, 'rising': 0}, 'astronomy': {'sunrise': '5:28 am', 'sunset': '7:23 pm'}, 'condition': {'text': 'Sunny', 'code': 32, 'temperature': 90}, 'pubDate': 1593572400}
forecasts : [{'day': 'Wed', 'date': 1593541800, 'low': 85, 'high': 103, 'text': 'Sunny', 'code': 32}, {'day': 'Thu', 'date': 1593628200, 'low': 89, 'high': 108, 'text': 'Mostly Sunny', 'code': 34}, {'day': 'Fri', 'date': 1593714600, 'low': 91, 'high': 110, 'text': 'Mostly Sunny', 'code': 34}, {'day': 'Sat', 'date': 1593801000, 'low': 88, 'high': 103, 'text': 'Partly Cloudy', 'code': 30}, {'day': 'Sun', 'date': 1593887400, 'low': 85, 'high': 99, 'text': 'Partly Cloudy', 'code': 30}, {'day': 'Mon', 'date': 1593973800, 'low': 84, 'high': 101, 'text': 'Partly Cloudy', 'code': 30}, {'day': 'Tue', 'date': 1594060200, 'low': 86, 'high': 101, 'text': 'Partly Cloudy', 'code': 30}, {'day': 'Wed', 'date': 1594146600, 'low': 84, 'high': 97, 'text': 'Thunderstorms', 'code': 4}, {'day': 'Thu', 'date': 1594233000, 'low': 84, 'high': 96, 'text': 'Thunderstorms', 'code': 4}, {'day': 'Fri', 'date': 1594319400, 'low': 85, 'high': 97, 'text': 'Thunderstorms', 'code': 4}]


"""

import pandas as pd
#dt =pd.json_normalize()
#res=list(result)
#dt1=json.dumps(result)
#print(type(result) , type(dt1))

#####################################################33

people_string='''
{
	"people": [
		{
			"id": 2002,
			"e_id": "'101'",
			"name": "'Vishal'",
			"time": "9/2/20 1:34 PM",
			"subject": "<pycharm><learrning>",
			"email" :true
		},
		{
			"id": 2003,
			"e_id": "'101'",
			"name": "'kelly'",
			"time": "9/3/20 1:34 PM",
			"subject": "<pandas><learrning>",
			"email":null
		}
	]
}
'''

#print(type(people_string))
data=json.loads(people_string)
#print(type(data) , data)
#print(type(data['people']) )
for dt in data['people']:
  print (dt['name'])

####
for dt in data['people']:
  del dt['email']

jsn_dmp=json.dumps(data ,indent=2 ,sort_keys=False)
print(jsn_dmp)

p()

with open('../Importingdata/files/test.json') as f:
  data =json.load(f)
  print(data)

p()
for forcast in data['forecasts']:
  print (forcast)
  del forcast['high']

  with open('../Importingdata/files/test1.json' ,'w') as f:
    json.dump(data ,f ,indent=2)

p()
c1='https://jsonplaceholder.typicode.com/todos'
with urlopen(c1) as response:
  source=response.read()

print(source)
dt_lds=json.loads(source)
dt_dmp=json.dumps(dt_lds ,indent=2)
print(type(dt_lds), type(dt_dmp))

for dt in dt_lds:
  for i in dt:
    print("title :" , dt["title"])


#data=json.loads(w1.get_yahoo_weather("buenos aires"))
#print(data)

