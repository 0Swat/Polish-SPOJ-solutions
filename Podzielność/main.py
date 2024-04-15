def answer(n, x, y):
    numbers = []
    for i in range(x, n, x):
        if i%y != 0:
            numbers.append(i)
    print(' '.join(map(str, numbers)))

def main():
    t = int(input())
    while t:
        n, x, y = map(int, input().split())
        answer(n, x, y)
        t-=1

if __name__ == '__main__':
    main()