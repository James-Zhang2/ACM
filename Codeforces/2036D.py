for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [input() for __ in range(n)]

    p = min(n, m) // 2
    k = 0
    for s in range(p):
        imin, jmin, imax, jmax = s, s, n - s, m - s
        res_s = a[imin][jmin:jmax]
        for i in range(imin+1, imax-1):
            res_s += a[i][jmax-1]
        res_s += a[imax-1][jmax-1:jmin:-1] + a[imax-1][jmin]
        for i in range(imax-2, imin, -1):
            res_s += a[i][jmin]
        res_s += res_s[:3]
        k += res_s.count("1543")
    print(k)
# 顺时针遍历数字，详见原题
