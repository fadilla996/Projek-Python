#for f in range(10):
#    print(f)
#    print(-f)

def rumah(x):
    x=x+1
    if x<3:
        rumah(x)
    x=x+2
    return x

rumah(1)