def string_merge(txt1, txt2):
    txt = ''
    l = len(txt1)
    if len(txt2) < l:
        l = len(txt2)

    for i in range(l):
        txt += txt1[i]
        txt += txt2[i]

    return txt

t = int(input())
for _ in range(t):
    t1, t2 = input().split()
    print(string_merge(str(t1), str(t2)))