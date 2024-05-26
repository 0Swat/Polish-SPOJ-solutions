import itertools

litery = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'c', 'z']
    ]

def Wyrazy(kombinacja):
    tablica = []
    litery_use = []

    for i in range(len(kombinacja)):
        litery_use.append(litery[int(kombinacja[i])-2])

    combinations = itertools.product(*litery_use)
    for combination in combinations:
        tablica.append(''.join(combination))

    return tablica


def main():
    n, k = map(int, input().split())
    wyrazy = []
    for _ in range(n):
        wyrazy.append(str(input()))
    print(wyrazy)
    kombinacje = Wyrazy('56567')
    print(kombinacje)


if __name__ == '__main__':
    main()