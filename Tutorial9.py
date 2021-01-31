file=open("C:\\Users\\LENOVO\\Desktop\\dilla\\dilla.txt","r")
#print(dir(f))
#print(f.read())
#f.seek(0)
#print(f.read())
#f.seek(1)
#print(f.read())
#a=file.readlines()
#file.seek(0)
#print(file.readline())
#print(file.readline())

#for f in a:
#    print(f)
print("a")
print("b")

for f in file:
    print(f,end="")

file.close()

file1=open("C:\\Users\\LENOVO\\Desktop\\dilla\\contohappend.txt","a")
file1.write("haha")
file2=open("C:\\Users\\LENOVO\\Desktop\\dilla\\filewrite.txt","w")
file2.write("haha")

file2.writelines(("Nama saya Dilla", "saya berburu makanan gratis"))

file1.close()
file2.close()

