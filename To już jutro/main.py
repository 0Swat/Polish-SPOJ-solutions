def Answer(l, c):
    if c%l == 0:
        print("TAK")
    else:
        print("NIE")

def main():
    t = int(input())
    while t:
        l, c = map(int, input().split())
        Answer(l, c)
        t-=1

if __name__ == '__main__':
    main()