#Tuples are immutables sequence of arbitrary objects
import copy

a=(2,4,6,8)
print (f'type of a is: {type(a)}' ,f' and value of a is:{a}' ,f' and length of a is:{len(a)}')

for i in a:
    print("values in For loop :" , i)

#  b=3   is int   and now tuple b=(3,)
c=(3,4,5)
# asssigning multiple value
c1,c2,c3=c
print("Prinitng values for c1,c2,c3:" ,c1,c2,c3)

#looking for value
d=('vishal' ,8,2.5,None)
print( "checking if 8 in Tuple d ",8 in d)

# mutlipling values
print("Tuples multipling c=(3,4,5) * 3 -----> " , c * 3)
