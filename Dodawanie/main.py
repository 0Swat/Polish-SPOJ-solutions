def main():
    t = int(input())
    while t:
        a, b = map(int, input().split())
        wynik = a+b
        print(wynik)
        t-=1

if __name__ == '__main__':
    main()