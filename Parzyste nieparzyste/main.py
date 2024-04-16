def answer(numbers):
    return_numbers = []
    for i in range(2, len(numbers), 2):
        return_numbers.append(numbers[i])
    for i in range(1, len(numbers), 2):
        return_numbers.append(numbers[i])
    print(' '.join(map(str, return_numbers)))

def main():
    n = int(input())
    while n:
        numbers = list(map(int, input().split()))
        answer(numbers)
        n-=1

if __name__ == '__main__':
    main()