def Solution(x):
    return x*x

def main():
    d = int(input())
    while d:
        print(Solution(int(input())))
        d-=1

if __name__ == '__main__':
    main()