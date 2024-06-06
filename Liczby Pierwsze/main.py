import math

def CzyLiczbaPierwsza(n):
    if n == 1:
        return 'NIE'
    m = abs(math.sqrt(n))
    i = 2
    while True:
        if i <= m:
            if n % i == 0:
                return 'NIE'
            else:
                i+=1
        else:
            return 'TAK'

def main():
    n = int(input())
    for _ in range(n):
        print(CzyLiczbaPierwsza(int(input())))

if __name__ == '__main__':
    main()