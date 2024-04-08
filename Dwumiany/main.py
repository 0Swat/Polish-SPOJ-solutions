def answer(n, k):
    if k == 0:
        return 1
    n_k = n-k
    n_silnia_k_silnia = 1
    k_silnia = 1
    for i in range(n_k+1, n+1):
        n_silnia_k_silnia*=i
    for i in range(1, k+1):
        k_silnia*=i

    return int(n_silnia_k_silnia / k_silnia)

def main():
    t = int(input())
    while t:
        n, k = map(int, input().split())
        print(answer(n, k))
        t-=1

if __name__ == '__main__':
    main()