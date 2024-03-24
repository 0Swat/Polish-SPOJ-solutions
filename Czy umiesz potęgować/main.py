def LastDigitPower(a, b):
    if b == 0:
        return 1
    n = a%10
    if n == 1:
        return 1
    elif n == 2:
        wynik = [4, 8, 6, 2]
        return wynik[(b%4)-2]
    elif n == 3:
        wynik = [9, 7, 1, 3]
        return wynik[(b%4)-2]
    elif n == 4:
        wynik = [6, 4]
        return wynik[(b%2)-2]
    elif n == 5:
        return 5
    elif n == 6:
        return 5
    elif n == 7:
        wynik = [9, 3, 7, 1]
        return wynik[(b%4)-2]
    elif n == 8:
        wynik = [4, 2, 6, 8]
        return wynik[(b%4)-2]
    elif n == 9:
        wynik = [1, 9]
        return wynik[(b%2)-2]
    elif n == 0:
        return 0
    

t = int(input())
for _ in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    print(LastDigitPower(a, b))