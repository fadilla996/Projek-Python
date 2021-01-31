class orang:
    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur

    def jalan(self):
        print("orang jalan")

    def makan(self):
        print(self.nama+" suka makan")

    def umurs(self, nama):
        print("umur teman "+nama+" "+str(self.umur)+" tahun")

class orangtua(orang):
    def __init__(self,nama,umur,waktumati):
        self.nama=nama
        self.umur=umur
        self.waktumati=waktumati
    def sakit(self):
        print(self.nama+" suka sakit sakitan")
    def makan(self):
        print(self.nama + " Cuma bisa makan bubur")

class orangorang:
    def __init__(self,*args):
        self.arg = args
        self.counter = 0
    def __iter__(self,*args):
        self.a = self.args[self.counter]

    def __next__(self):
        self.counter += 1
        x = args[self.counter]
        return x

def penjumlahan(a,b):
    sum=a+b
    return sum

def pengurangan(a,b):
    min=b-a
    return min