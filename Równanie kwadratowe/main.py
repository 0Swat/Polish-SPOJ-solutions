def answer(a, b, c):
    delta = b*b - 4*a*c
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0


def main():
    while True:
        try:
            a, b, c = map(float, input().split())
            print(answer(a, b, c))
        except EOFError:
            break

if __name__ == '__main__':
    main()