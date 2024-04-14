def T(A):
    wynik = []
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        print(' '.join(map(str, temp)))

def main():
    A = []
    m, n = map(int, input().split())
    while m:
        a = list(map(int, input().split()))
        A.append(a)
        m-=1
    T(A)

if __name__ == '__main__':
    main()