#import modul
#from modul import *
#from modul import penjumlahan,pengurangan
import modul as md
#import Bubblesort as bs

#haha=1
#hehe=2
#print(modul.penjumlahan(haha,hehe))

#y=[1,23,123,43,23,43,12,12,11,31]
#print(bs.bubblesort(y))

#print(penjumlahan(haha,hehe))
#md.penjumlahan(1,2)
#bs.penjumlahan(1,2)

a=17
a=float(17)

Awla=md.orang("Awla",17)
print(Awla.nama)
print(Awla.umur)
Awla.jalan()
Awla.makan()
Awla.umurs("Nico")

Fuad = md.orangtua("Fuad", 89,100)
print(Fuad.nama)
Fuad.jalan()
Fuad.sakit()
Fuad.makan()

komunitas = md.orangorang("Awla","Fajri","Assalam")
print(komunitas.arg)
for f in komunitas.arg:
    print(f)