def DwieCyfrySlnia(liczba):
    if liczba >= 10:
        print(0, 0)
        return
    wynik = 1
    for i in range(1, liczba+1):
        wynik = wynik*i
        wynik = wynik%100
    print(int((wynik/10)%10), int(wynik%10))
    return

t = int(input())
for _ in range(t):
    x = int(input())
    DwieCyfrySlnia(x)