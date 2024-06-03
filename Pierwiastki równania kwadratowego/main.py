from decimal import Decimal, getcontext

def answer(a, b, c, k):
    getcontext().prec = k+50
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    delta = (b * b) - (4 * a * c)
    if delta < 0 or a == 0:
        print(0)
    elif delta == 0:
        x = -b / (2 * a)
        print('1 {}'.format(x))
    elif delta > 0:
        sqrt_delta = Decimal(delta).sqrt()
        x1 = (-b - sqrt_delta) / (2 * a)
        x2 = (-b + sqrt_delta) / (2 * a)

        if x2 > x1:
            print('2 {} {}'.format(x1, x2))
        else:
            print('2 {} {}'.format(x2, x1))

def main():
    t = int(input())
    while t:
        a, b, c, k = map(int, input().split())
        answer(a, b, c, k)
        t-=1
    return

if __name__ == '__main__':
    main()