import sys
sys.setrecursionlimit(10 ** 4)

def f(i, j):
    global s, flag, otv
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    if flag[i][j] == 1:
        return 1
    if flag[i][j] == 2:
        return otv[i][j]
    flag[i][j] = 1
    if s[i][j] == 'U':
        q = f(i - 1, j)
    elif s[i][j] == 'D':
        q = f(i + 1, j)
    elif s[i][j] == 'R':
        q = f(i, j + 1)
    elif s[i][j] == 'L':
        q = f(i, j - 1)
    else:
        q = f(i + 1, j) or f(i - 1, j) or f(i, j + 1) or f(i, j - 1)
    if q:
        otv[i][j] = 1
        return 1
    flag[i][j] = 2
    return 0


for _ in range(int(input())):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(list(map(str, input())))
    flag = []
    otv = []
    for i in range(n):
        flag.append([0] * m)
        otv.append([0] * m)
    for i in range(n):
        for j in range(m):
            f(i, j)
    count = 0
    for i in range(n):
        for j in range(m):
            if otv[i][j] == 1:
                count += 1
    print(count)
