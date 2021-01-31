def inputdata():
    x = int(input("masukan angka :"))
    return x

def kalkulasi(x):
    y = [0,0,0]
    y[1]=x+2
    y[2]=3*x+1
    y[0]=x**2+2*x+1
    print(y)
    return y

def printdata(asal):
    for f in asal :
        print(f)

printdata(kalkulasi(inputdata()))
printdata(kalkulasi(inputdata()))
