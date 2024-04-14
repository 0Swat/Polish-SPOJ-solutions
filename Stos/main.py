class Stos:
    def __init__(self):
        self.rozmiar = 10
        self.tablica = []

    def Dodaj(self, znak):
        if len(self.tablica) >= self.rozmiar:
            print(":(")
        else:
            self.tablica.append(znak)
            print(":)")
    
    def Usun(self):
        if len(self.tablica) == 0:
            print(":(")
        else:
            print(self.tablica[len(self.tablica)-1])
            self.tablica.pop(len(self.tablica)-1)
def main():
    stos1 = Stos()
    while True:
        try:
            znak = input()
            if znak == "+":
                liczba = int(input())
                stos1.Dodaj(liczba)
            if znak == "-":
                stos1.Usun()
        except EOFError:
            break

if __name__ == '__main__':
    main()