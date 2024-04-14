def shift(tab, k):
    out = []
    for i in range(len(tab)): 
       out.append(tab[(i+k)%len(tab)])
    print(' '.join(map(str, out)))
    

def main():
    n, k = map(int, input().split())
    tablica = list(map(int, input().split()))
    shift(tablica, k)

if __name__ == '__main__':
    main()
