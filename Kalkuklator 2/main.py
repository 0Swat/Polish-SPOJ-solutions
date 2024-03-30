rejestr = [0 for _ in range(10)]

def Zapis(index, liczba):
    rejestr[index] = liczba

def Kalkulator():
    while True:
        try:
            znak, a, b = input().split()
            znak, a, b = str(znak), int(a), int(b)
            if znak == "z":
                Zapis(a, b)
            elif znak == "+":
                print(int(rejestr[a]+rejestr[b]))
            elif znak == "-":
                print(int(rejestr[a]-rejestr[b]))
            elif znak == "*":
                print(int(rejestr[a]*rejestr[b]))
            elif znak == "/":
                print(int(rejestr[a]/rejestr[b]))
            elif znak == "%":
                print(int(rejestr[a]%rejestr[b]))
        except EOFError:
            break


Kalkulator()