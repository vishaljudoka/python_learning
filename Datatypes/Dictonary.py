###Dictonaries
from need import *

from Datatypes.need import p

logs={'Prod' : ('info','warning'),
       'UAT' : ('info','warning','Error'),
       'DEV' : ('info','warning','Error','Failed')}
a,b=(logs['Prod'])
print("a=",a,"b=",b)

p()
print (f'type of logs is: {type(logs)}'  ,f' and length of logs is:{len(logs)}')
for i in logs:
        print("key is {} and value is {} ".format (i, logs[i]))
p()

## copy for dict
ba={'Prod' : ('info','warning'),
       'UAT' : ('Error'),
       'DEV' : ('Failed')}

ca=ba.copy()
print("ca=ba then ca is ba :",ca is ba ,"value check :",ca == ba)
da=dict(ca)
print("da=ba then da is ba :",da is ba ,"value check :",da == ba)
p()

###add value to same key
ca.update({'SAT':'All'})
print("ca.update({'SAT':'All'})  after : " ,ca)
ca ['Prod'] +=('read',)
print(ca)


