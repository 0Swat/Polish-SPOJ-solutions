def answer(a, b, c, k):
    print(a, b, c, k)

def main():
    t = int(input())
    while t:
        a, b, c, k = map(int, input().split())
        answer(a, b, c, k)
        t-=1
    return

if __name__ == '__main__':
    main()