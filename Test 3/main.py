def main():
    licznik = 0
    liczba1 = int(input())
    print(liczba1)
    while licznik < 3:
        liczba2 = int(input())
        if liczba2 == 42 and liczba1 != 42:
            licznik+=1
        liczba1 = liczba2
        print(liczba1)

if __name__ == '__main__':
    main()