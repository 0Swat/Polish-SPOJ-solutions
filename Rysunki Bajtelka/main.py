def pole(liczby):
    liczby.pop()
    liczby.pop()
    wynik = 0
    for i in range(0, len(liczby)-2, 2):
        xi = liczby[i]
        yi = liczby[i+1]
        xi_1 = liczby[i+2]
        yi_1 = liczby[i+3]
        wynik += ((xi*yi_1 - xi_1*yi))
    x1 = liczby[0]
    xn = liczby[len(liczby)-2]
    y1 = liczby[1]
    yn = liczby[len(liczby)-1]
    wynik += (xn*y1 - x1*yn)
    if wynik < 0:
        wynik *= -1
    wynik /= 2
    return wynik

def answer(pole_czarne, pole_szare):
    cena_czarne = 10
    cena_szare = 6
    pole_szare -= pole_czarne
    wynik = (cena_czarne * pole_czarne) + (cena_szare * pole_szare)
    return int(wynik)

def main():
    t = int(input())
    while t:
        liczby1 = list(map(int, input().split()))
        liczby2 = list(map(int, input().split()))
        print(answer(pole(liczby1), pole(liczby2)))
        input()
        t-=1

if __name__ == '__main__':
    main()