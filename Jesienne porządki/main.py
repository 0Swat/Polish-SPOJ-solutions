import math


def mediana(data):
    if len(data)%2==0:
        return data[int(len(data)/2-1)][0]
    else:
        return data[int(len(data)/2)][0]

def main():
    n = int(input())
    kopce = []
    while n:
        x, y = map(int, input().split())
        kopiec = (x, y)
        kopce.append(kopiec)
        n-=1

    kopce.sort(key=lambda x: x[0])

    print(kopce)
    print(mediana(kopce))


    return

if __name__ == '__main__':
    main()