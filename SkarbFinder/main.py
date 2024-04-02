def Odpowiedz(x, y):
    if x == 0 and y == 0:
        print("studnia")
    if x == 0 and y != 0:
        if y > 0:
            print(3, y)
        else:
            print(2, y*-1)
    if x != 0 and y == 0:
        if x > 0:
            print(0, x)
        else:
            print(1, x*-1)
    if x != 0 and y != 0:
        if x > 0:
            print(0, x)
        else:
            print(1, x*-1)
        if y > 0:
            print(3, y)
        else:
            print(2, y*-1)

d = int(input())
while d:
    n = int(input())
    x, y = 0, 0
    while n:
        a, b = map(int, input().split())
        if a == 0:
            x += b
        if a == 1:
            x -= b
        if a == 2:
            y -= b
        if a == 3:
            y += b
        n-=1
    Odpowiedz(x, y)
    d-=1