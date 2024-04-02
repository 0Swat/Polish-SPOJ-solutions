class Uklad:
    def __init__(self, n):
        self.punkty = []
        
    def DodajPunkt(self, nazwa, x, y):
        odleglosc = (x**2 + y**2)**0.5
        self.punkty.append([str(nazwa), int(x), int(y), odleglosc])

    def PosortujIPokaz(self):
        posortowane = self.punkty
        posortowane.sort(key=lambda x: x[3])
        for punkt in posortowane:
            print(punkt[0], punkt[1], punkt[2])

def main():
    t = int(input())
    while t:
        n = int(input())
        uklad = Uklad(n)
        while n:
            nazwa, x, y = input().split()
            nazwa, x, y = str(nazwa), int(x), int(y)
            uklad.DodajPunkt(nazwa, x, y)
            n-=1
        uklad.PosortujIPokaz()
        input()
        t-=1

if __name__ == '__main__':
    main()