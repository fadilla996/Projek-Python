from kelas import *

#dir=str(input("Masukkan direktori file : \n"))
testfile=open("C:\\users\\LENOVO\\Desktop\\dilla\\tesmainan.txt","r",encoding="utf 8")
print(testfile.read())

testfile.seek(0)
counts={}
for baris in testfile:
    katakata = baris.split(" ") #nama saya Dilla rumah: -> [nama,saya,Dilla, rumah:, rumah-rumah]
    for kata in katakata: #nama->saya->Dilla->rumah
        for katabersih in ilanginsimbol(kata): #nama-> nama, rumah: -> rumah, rumah-rumah -> [rumah,rumah]
            counts[katabersih.lower()]=counts.get(katabersih.lower(),0)+1
print(counts)

kataterbanyak=str()
jumlahkata=0

for f in counts.keys():
    if counts[f]>jumlahkata:
        kataterbanyak=f
        jumlahkata=counts[f]

print(kataterbanyak,":",jumlahkata)
