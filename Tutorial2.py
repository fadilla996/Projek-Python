import math

a=12
b=12.4

#print(type(a))
#a=float(a)
#print(a)
#print(type(a))

b=int(b)
print(b)

c=b/a
print(c)
print(dir(float))

a=2
b=2.0
print(a==b)

string = "saya suka burung perkutut"
print("saya" in string)

counter = 0
string = "saya suka burung perkutut"
for f in string:
    if(f=="s"):
        counter+=1
print(counter)

c=a**b
d=math.pow(a,b)
print(dir(math))
print(c)
print(d)