def Oblicz(s):
    i = 0
    while s != 1:
        if s%2==0:
            s /= 2
        else:
            s = 3*s+1
        i+=1
    return i


t = int(input())
while t:
    print(Oblicz(int(input())))
    t-=1