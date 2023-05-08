#Tuples are immutables sequence of arbitrary objects
import copy
import math
import datetime

from Datatypes.need import p

line=p()

a="Vishal"
print (f'type of a is: {type(a)}' ,f' and value of a is :{a}' ,f' and length of a is :{len(a)}')
p()
for i in a:
    print("values in For loop :" , i)
p()
#looking for value
d='vishal'
print( "checking if i in str d='vishal'",i in d)
p()
# mutlipling values
print("Str multipling d='Vishal' * 3 -----> " , d * 3)
p()
#Join  in str

c= (['this','is','example' ,'to','join'])
d=';'.join(c)
print("Str Join = ",d)
p()
#spilt in strings reult into list
print('vishal, is, good'.split(','))
print("this is split result in list =" ,d.split(';'))
p()
# partioning of Strings result in tuple
par="Vishal".partition('sh')
print("partiting eg type and value:" , type(par) , par)
p()
start,middle,end=("Vishal".partition('sh'))
print("partiting value :","start:",start,"middle:", middle,"end:", end)
p()


###strip
print("(Lstrip ==>" ,"Lstrip".lstrip("(L")    ,"\nRstrip:) ==>" ,"Rstrip :)".rstrip(":)" ), "\n(St-rip-) ==>"  , "(Str-ip-)".strip("(-)"))

###String Format
print("The age of {0} is {1}".format('Vishal',30))
p()
print("The age of {anda} is {banda}".format(anda='sara',banda=3))
p()
print("math constnts : pi={m.pi:.3f} and e={m.e:.3f}".format(m=math))   ##floating point format 3f
p()

print (f'The age of spatrcus is :{30*10}')
print ("The age of spatrcus is :{age} ".format(age=1*3*100))

print(f'datetime using fstings is :{datetime.datetime.now().isoformat()}')
p()

str_en="Hello".encode()
str_dec=str_en.decode()
print("Encode Type :" , type(str_en) ," and value is :" ,str_en)
print("Decode Type :" , type(str_dec) ," and value is :" ,str_dec)

