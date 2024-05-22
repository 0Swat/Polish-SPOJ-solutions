def main():
    n = int(input())
    suma, makskasa = 0, 0
    while n:
        zysk = int(input())
        suma += zysk
        if suma > makskasa:
            makskasa = suma
        if suma < 0:
            suma = 0
        n-=1
    print(makskasa)



if __name__ == '__main__':
    main()