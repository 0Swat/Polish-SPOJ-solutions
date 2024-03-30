def Kalkulator():
    while True:
        try:
            func, a, b = input().split()
            a, b = int(a), int(b)
            if func == "+":
                print(int(a+b))
            if func == "-":
                print(int(a-b))
            if func == "*":
                print(int(a*b))
            if func == "/":
                print(int(a/b))
            if func == "%":
                print(int(a%b))
        except:
            break

Kalkulator()