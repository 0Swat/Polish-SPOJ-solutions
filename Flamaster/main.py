def DodajLiterka(literka, ilosc):
    if ilosc == 0:
        return ''
    elif ilosc == 1:
        return literka
    elif ilosc == 2:
        return literka+literka
    else:
        return literka+str(ilosc)

def ShortWord(wyraz_in):
    dlugosc = len(wyraz_in)
    wyraz_out = ''
    licznik = 1
    i = 0

    while i < dlugosc:
        if i + 1 < dlugosc and wyraz_in[i] == wyraz_in[i + 1]:
            licznik += 1
        else:
            wyraz_out += DodajLiterka(wyraz_in[i], licznik)
            licznik = 1
        i += 1

    return wyraz_out

t = int(input())
for _ in range(t):
    slowo = input()
    print(ShortWord(slowo))
