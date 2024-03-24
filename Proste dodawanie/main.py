def NSum(n, N):
    suma = 0
    for i in range(n):
        suma += N[i]
    return suma

num = int(input())
for _ in range(num):
    n = int(input())
    suma = 0
    numbers = list(map(int, input().split()))
    print(NSum(n, numbers))