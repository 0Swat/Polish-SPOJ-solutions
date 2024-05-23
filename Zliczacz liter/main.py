import string

def main():
    znaki = []
    maly_alfabet = string.ascii_letters
    for i in range(len(maly_alfabet)):
        znaki.append(maly_alfabet[i])
        znaki.append(0)
    
    n = int(input())
    while n:
        text = str(input())
        for i in range(len(text)):
            literka = text[i]
            for j in range(len(znaki)):
                if znaki[j] == literka:
                    znaki[j+1] += 1
        n-=1
    
    for i in range(1, len(znaki), 2):
        if znaki[i] != 0:
            print(znaki[i-1], znaki[i])

if __name__ == '__main__':
    main()