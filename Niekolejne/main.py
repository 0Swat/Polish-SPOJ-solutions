def answer(n):
    if n <= 2 and n != 0:
        print("NIE")
    else:
        tablica = []
        for i in range(1, n+1, 2):
            tablica.append(i)
        for i in range(0, n+1, 2):
            tablica.append(i)
        print(" ".join(map(str, tablica)))
    
def main():
    n = int(input())
    answer(n)
    
if __name__ == '__main__':
    main()