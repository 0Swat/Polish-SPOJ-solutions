def answer(data):
    kopiec = mediana(data)
    dlugosc = 0

    for i in range(len(data)):
        dlugosc += length(data[i], kopiec)
        
    print(str(kopiec) + " " + str(dlugosc))


def length(punkt, x):
    dlugosc_x = abs(punkt[0] - x)
    dlugosc_y = abs(punkt[1])

    return dlugosc_x + dlugosc_y

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

    answer(kopce)

if __name__ == '__main__':
    main()