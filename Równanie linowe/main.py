def answer(a, b, c):
    if b == c and a == b:
            return "NWR"
    if a == 0.0:
        if b == c:
            return "NWR"
        return "BR"
    x = (c - b)/a
    return round(x, 2)

def main():
    a, b, c = map(float, input().split())
    print(answer(a, b, c))

if __name__ == '__main__':
    main()