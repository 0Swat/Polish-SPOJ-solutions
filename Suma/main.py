def Suma():
    suma = 0 
    while True:
        try:
            liczba = int(input())
            suma += liczba
            print(suma)
        except:
            break

def main():
    Suma()

if __name__ == '__main__':
    main()