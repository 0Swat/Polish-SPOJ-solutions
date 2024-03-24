def PredkoscSrednia(v1, v2):
    v = (2 * v1 * v2) / (v1 + v2)
    return int(v)

t = int(input())
for i in range(t):
    a, b = input().split()
    print(PredkoscSrednia(int(a), int(b)))