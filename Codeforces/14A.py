n, m = map(int, input().split())
g = [input() for i in range(n)]
x = []
y = []
for i in range(n):
    for j in range(m):
        if g[i][j] == '*':
            x.append(i)
            y.append(j)
        # 这是一个很好的处理方法
a, b, c, d = min(x), max(x), min(y), max(y)
for i in range(a, b + 1):
    print(g[i][c:d+1])
# 处理多行数据输入输出时可以先开i, n 和 j, m 遍历列表，再输出ls[i][j]
