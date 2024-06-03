def answer(a, b, c, k):
    delta = b*b - 4*a*c
    if delta < 0:
        print('0')
    elif delta == 0:
        x = -b / 2*a
        print('1 ' + str(x))
    elif delta > 0:
        x1 = (-1*b - delta**0.5) / 2*a
        x2 = (-1*b + delta**0.5) / 2*a
        print('2 ' + str(x1) + ' ' + str(x2))

def main():
    t = int(input())
    while t:
        a, b, c, k = map(int, input().split())
        answer(a, b, c, k)
        t-=1
    return

if __name__ == '__main__':
    main()