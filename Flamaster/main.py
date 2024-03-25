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
    licznik = 0
    literka = ''

    for i in range(dlugosc):
        literka = wyraz_in[i]
        if i == dlugosc-1 and i != 0:
            licznik += 1
            wyraz_out += DodajLiterka(literka, licznik)
        else:
            if wyraz_in[i+1] == literka:
                licznik += 1
            else:
                licznik += 1
                wyraz_out += DodajLiterka(literka, licznik)
                licznik = 0

    return str(wyraz_out)

t = int(input())
for _ in range(t):
    slowo = str(input())
    print(ShortWord(slowo))