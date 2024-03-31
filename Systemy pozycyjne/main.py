def Konwersja(liczba, system):
    znaki = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    output = ''

    while liczba:
        output = znaki[liczba%system] + output
        liczba = int(liczba / system)
    
    return output

t = int(input())
while t:
    liczba = int(input())
    print(Konwersja(liczba, 16), Konwersja(liczba, 11))
    t-=1