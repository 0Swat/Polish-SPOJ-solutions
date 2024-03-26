def NWD(a, b):
    while(b):
        a, b = b, a%b
    return a

def NWW(a, b):
    return int((a*b) / NWD(a, b))

t = int(input())
while t:
    a, b = input().split()
    print(NWW(int(a), int(b)))
    t-=1