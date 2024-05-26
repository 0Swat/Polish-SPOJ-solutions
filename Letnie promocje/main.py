litery = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

def WyrazNaKombinacje(wyraz):
    kombinacja = ''
    for k in range(len(wyraz)):
        literka = wyraz[k]
        for i in range(len(litery)):
            for j in range(len(litery[i])):
                if literka == litery[i][j]:
                    kombinacja += str(i + 2) 
    return kombinacja

def main():
    n, k = map(int, input().split())
    wyrazy = []
    kombinacje = []
    kombinacje_in =[]

    for _ in range(n):
        wyraz = str(input())
        wyrazy.append(wyraz)
        kombinacje.append(WyrazNaKombinacje(wyraz))
    for _ in range(k):
        kombinacje_in.append(str(input())) 

    for i in range(len(kombinacje_in)):
        znaleziono = False
        znalezione_wyrazy = []
        for j in range(len(kombinacje)):
            if kombinacje_in[i] == kombinacje[j]:
                znaleziono = True
                znalezione_wyrazy.append(wyrazy[j])
        if znaleziono == False:
            print("BRAK")
        else:
            znalezione_wyrazy.sort()
            print(' '.join(znalezione_wyrazy))



if __name__ == '__main__':
    main()