def answer(liczby):
    liczby2 = []
    for i in range(len(liczby)):
        liczby2.append(liczby[len(liczby)-i-1])
    print(' '.join(map(str, liczby2)))

def main():
    liczby = list(map(int, input().split()))
    answer(liczby)

if __name__ == '__main__':
    main()