import copy

def answer(array, l, k):
    new_array = copy.deepcopy(array)

    for i in range(l):
        for j in range(k):
            if i == 0 and j < k-1:
                array[i][j] = new_array[i][j+1]
            elif i < l-1 and j == k-1:
                array[i][j] = new_array[i+1][j]
            elif i == l-1 and j > 0:
                array[i][j] = new_array[i][j-1]
            elif i > 0 and j == 0:
                array[i][j] = new_array[i-1][j]

    for i in range(l):
        print(" ".join(map(str, array[i])))
    

def main():
    t = int(input())
    while t:
        array = []
        l, k = map(int, input().split())
        j = l
        while j:
            num = list(map(int, input().split()))
            array.append(num)
            j-=1
        answer(array, l, k)
        t-=1

if __name__ == '__main__':
    main()