#Range sequence representing  an arthmetic progression of integar
"""
range(5) #stop
range(1,5) #start ,Stop
range(1,10,2) #start stop step
"""
for i in range(1,10,2):
    print(i)

###Enumerate  (Index and value)
a=[3,4,5,8,'a']
for i,v in enumerate(a) :
    print (f' i={i}, v={v}')
