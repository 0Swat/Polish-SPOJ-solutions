def answer(tab):
    avg = sum(tab)/len(tab)
    output = tab[0]
    for i in range(1, len(tab)):
        if abs(tab[i] - avg) < abs(output - avg):
            output = tab[i]
    print(output)

def main():
    t = int(input())
    while t:
        num = list(map(int, input().split()))
        answer(num[1::])
        t-=1

if __name__ == '__main__':
    main()