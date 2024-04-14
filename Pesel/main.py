def answer(pesel):
    cyferki = []
    mnozniki = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    suma = 0
    for i in range(10, -1, -1):
        cyferki.append(int(pesel/(10**i)))
        pesel -= int(pesel/(10**i)) * (10**i)

    for i in range(11):
        suma += cyferki[i]*mnozniki[i]
    if suma%10 == 0: return "D"
    return "N"
def main():
    t = int(input())
    while t:
        print(answer(int(input())))
        t-=1

if __name__ == '__main__':
    main()