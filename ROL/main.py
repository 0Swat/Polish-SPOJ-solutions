def shift(n, tab):
    out = []
    for i in range(len(tab)): 
       out.append(tab[(i+1)%len(tab)])
    print(' '.join(map(str, out)))
    

def main():
    t = int(input())
    while(t):
        N = list(map(int, input().split()))
        n = N[0]
        x = [N[i] for i in range(1, len(N))]
        shift(n, x)
        t-=1

if __name__ == '__main__':
    main()
