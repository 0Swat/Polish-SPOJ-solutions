def Answer(l, c):
    c_len = len(c)
    temp = ''
    for i in range(c_len):
        if i != 0:
            temp = str(modulo)
        modulo = int(temp + c[i]) % l
    
    if modulo == 0:
        print("TAK")
    else:
        print("NIE")


def main():
    t = int(input())
    while t:
        l, c = map(int, input().split())
        Answer(l, str(c))
        t-=1

if __name__ == '__main__':
    main()