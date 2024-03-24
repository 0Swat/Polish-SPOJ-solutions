t = int(input())
tablica = []
for _ in range(t):
    tablia = input().split()
    rozmiar_tablicy = int(len(tablia))
    for i in range(0, int(tablia[0])):
        print(tablia[rozmiar_tablicy-1-i])
