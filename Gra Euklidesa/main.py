def answer(a, b):
    while b:
        tmp = a % b
        a = b
        b = tmp
    print(a*2)

def main():
    t = int(input())
    while t:
        a, b = map(int, input().split())
        answer(a, b)
        t-=1

if __name__ == '__main__':
    main()