##list are mutable
from need import p

a=[2,4.6,'vish',8]
print (f'type of a is: {type(a)}' ,f' and value of a is:{a}' ,f' and length of a is:{len(a)}')

p()
for i in a:
    print( i ," ",end="")
print()
p()
print("First element of ",a,"is=", a[0])
print("Last element of ",a,"is=",  a[len(a)-1])
p()
##check if values are equal
ab=a[-1]
ac=a[len(a)-1]
print(ab is ac)
p()
####Slice
##r[start:stop]
b=[3,6,7,8,9]
print("list b=",b)
print("b[2:]",b[2:] ,"-----", "b[:2]", b[:2] ," ------ b[2:4]", b[2:4] )
print("b[1:-1]",b[1:-1] )
p()

######copy
ba=[3,6,23,65,9]
ca=ba
print("ba=",ba,"ca=ba then ca is ba :",ca is ba ,"value check :",ca == ba)
ad=ba[:]
print("ba=",ba,"ad=ba[:] then ad is ba :",ad is ba ,"value check :",ad == ba)
aa=ba.copy()
print("ba=",ba,"aa=ba.copy() then aa is ba :",aa is ba ,"value check :",aa == ba)
p()

######appending value and checking if orinal object also change
print("appending value and checking if orginal object also change")

def append1(boo):
    mm=boo   ### to not change original object boo.copy()
    mm.append(10)
    return (mm)

bb=[13,6,23,65,9]
ca=bb
print("Before bb=",bb,"ca=",ca,"ca=bb then ca is ba :",ca is bb ,"----value check :",ca == bb)
ca=append1(bb)
print("After bb=",bb,"ca=",ca,"ca=bb then ca is ba :",ca is bb ,"----value check :",ca == bb)
p()
#######

###changing list itself and checking if original also change
print("Replacing argument value and checking if original also change")
def replace(baa):
    baa=['a','b']
    return baa

bbb=[13,6,23,65,9]
wca=bbb
print("Before" ,"bbb=",bbb,"wca=",wca,"wca=bbb then wca is ba :",wca is bbb,"----value check :",wca == bbb)
wca=replace(bbb)
print("After bbb=",bbb,"wca=",wca,"wca=bbb then wca is ba :",wca is bbb,"----value check :",wca == bbb)
p()

###changing value one by one
print("changing value one by one")
def change(aaa):
    for i in range(len(aaa)):
        aaa[i]=i*2
    return aaa

baa=[3,6,1,5,9]
wca=baa
print("Before" ,"baa=",baa,"wca=",wca,"wca=baa then wca is baa :",wca is baa,"----value check :",wca == baa)
wca=change(baa)
print("After baa=",baa,"wca=",wca,"wca=baa then wca is baa :",wca is baa,"----value check :",wca == baa)
p()

# c.count(4) , c.index('7')
# 4 in c
#### in Split str  it converts to list
c=[4,5,6,7]
b=[3,8]
del c[1]
print (f'del c[1] :{c}' )
print(f'c.count[4] is : {c.count(4)}' ,"in list c =",c)
print(f'c.index(7) is : {c.index(7)}' ,"in list c =", c)
print(f'4 in c is : {4 in c}' ," list c =" ,c)
print(f'c.remove(6) : {c.remove(6)}' ,"in list c =", c)
print(f'c.insert(5) : {c.insert(2,5)}' ,"in list c =", c)
print(f'c.extend(5) : {c.extend(b)}' ,"in list c =", c)
print(f'c.sort(5) : {c.sort(reverse=True)}' ,"in list c =", c)   #true or false asc and desc
print(f'c.pop(5) : {c.pop(0)}' ,"in list c =", c)
p()


