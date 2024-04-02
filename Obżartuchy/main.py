import math

def IleCiastek24H(czas_na_1):
    ciastka = 86400 / czas_na_1
    return int(ciastka)

def IleKupicPudelek(ilosc_ciastek, ile_w_pudelku):
    ilosc = ilosc_ciastek / ile_w_pudelku
    return int(math.ceil(ilosc))




t = int(input())
while t:
    n, m = input().split()
    n, m = int(n), int(m)
    ilosc_ciastek = 0
    while n:
        ilosc_ciastek += IleCiastek24H(int(input()))
        n-=1
    print(IleKupicPudelek(ilosc_ciastek, m))
    t-=1