def answer(a, b, c):
    if a == 0.0:
        if b == c:
            return "NWR"
        else:
            return "BR"
    else:
        x = (c - b) / a
        return f"{round(x, 2):.2f}"


def main():
    a, b, c = map(float, input().split())
    print(answer(a, b, c))

if __name__ == '__main__':
    main()