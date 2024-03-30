def Suma():
    suma = 0 
    while True:
        try:
            liczba = int(input())
            suma += liczba
            print(suma)
        except:
            break
Suma()