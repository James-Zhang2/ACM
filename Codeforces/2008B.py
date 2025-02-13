from math import sqrt
for _ in range(int(input())):
    n = int(input())
    mystr = input()
    a = sqrt(n)
    if a != int(a):
        print("No")
        continue
    b = int(a)
    ls = []
    for i in range(1, b-1):
        for j in range(1, b-1):
            ls.append(i * b + j)
    c = True
    for j in range(n):
        if j in ls:
            if mystr[j] != "0":
                c = False
                break
        else:
            if mystr[j] != "1":
                c = False
                break
    print("Yes" if c else "No")
# 审题不仔细，已经说了漂亮矩阵
