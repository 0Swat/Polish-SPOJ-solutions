def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

t = int(input())
for _ in range(t):
    x1, x2 = input().split()
    print(nwd_i(int(x1) , int(x2)))
