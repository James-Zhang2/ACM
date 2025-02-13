for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [x - 1 for x in list(map(int, input().split()))]
    b = [x - 1 for x in list(map(int, input().split()))]
    pos = a[:]
    for i in range(n):
        pos[a[i]] = i  # 得到一个索引数组
    lst = -1
    res = m  # 预处理，已经 将 每一项 都加上 1
    for i in range(m):
        if pos[b[i]] > lst:
            res += 2 * (pos[b[i]] - i)
            lst = pos[b[i]]
    print(res)
