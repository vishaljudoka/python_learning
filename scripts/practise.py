
alphalist=['a','b','c','d','e','f','g','h','i','j','k']
a=True
b=1
c=1.5
d='h'
e='hello'
f=(1,2,3,4,5,1,2,3,4)
g=[1,2,3,4,5,6,1,2,3,4,5,6]
h={1,2,3,4,56,3,1,3}
i={a:1,b:2,c:3}
j=range(1,10)
k=bytes(1)

print (type(a) ,": ",a)
print (type(b) ,": ",b)
print (type(c) ,": ",c)
print (type(d) ,": ",d)
print (type(e) ,": ",e)
print (type(f) ,": ",f)
print (type(g) ,": ",g)
print (type(h) ,": ",h)
print (type(i) ,": ",i)
print (type(j) ,": ",j)
print (type(k) ,": ",k)

for i in range(1,11,1):  # 10 (1-10)
  #print( i)
    pass
#
for k in range(10): # 9 (0-9)
   print( k)
#
#for j in range(0,8): # 8 (0-7)
#    print( j)


import csv
import os
from datetime import datetime

#####Reading CSV
file_location = os.path.join(os.getcwd(), 'file_upload', 'raw_price.csv')
file=open(file=file_location , newline="")
reader=csv.reader(file)

header=next(reader)
#data=[row for row in reader]

data=[]
for row in reader:
    #headerlist=[Date,Open,High,Low,Close,Volume]
    date_0=datetime.strptime(row[0] , '%m/%d/%Y')
    open_1=float(row[1])
    High_2=float(row[2])
    Low_3=float(row[3])
    Close_4=float(row[4])
    Volume_5=int(row[5])
    data.append([date_0,open_1,High_2,Low_3,Close_4,Volume_5])

print(data[0])


# Writing CSV
file_location = os.path.join(os.getcwd(), 'file_upload', 'temp_data1.csv')
file=open(file=file_location , mode='a' ,newline='', encoding='utf-8')
writer=csv.writer(file)
print(dir(csv))
line_to_add=[2021,13,12000]
writer.writerow(line_to_add)