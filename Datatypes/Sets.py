#set is unordered collection of unique elements
#mutable
#elements inside are inmutable
from need import p

a={3,4,5,6,7,7,7,8,9}
print (f'type of a is: {type(a)}' ,f' and value of a is:{a}' ,f' and length of a is:{len(a)}')
e={2,32,5,31}
d=set()
print("type of e =",type(e) , "type of d =", type(d))
p()
print (f'e.add(4) :{e.add(4)}' ,"e set=",e )
print(f'e.update(5) is : {e.update({1,2,3,4,5})}' ,"in set e =",e)
print (f'e.remove(4) :{e.remove(4)}' ,"e set=",e )    ###key error
print (f'e.discard(4) :{e.discard(4)}' ,"e set=",e )
p()
#####copy
f=(e.copy())
g={32,7,8,9}
print("e =" , e , "g=",g)
print( "e.union(g) :",e.union(g))
print( "e.difference(g) :",e.difference(g))
print( "e.symmetric_difference(g) :",e.symmetric_difference(g))
print( "e.issuperset(g) :",e.issuperset(g))
print( "e.issubset(g) :",e.issubset(g))
print( "e.isdisjoint(g) :",e.isdisjoint(g))
