t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = -1
    v = []
    for x in a:
        if x % 2 == 0:
            v.append(x)
        elif x > s:
            s = x  # 最大奇数
    v.sort()
    if s == -1 or v == []:  # 无奇数 or 无偶数
        print(0)
        continue
    ans = len(v)
    for t in v:
        if t < s:
            s += t  # 模拟最大奇数的迭代，有偶数比它大则 ans += 1
        else:
            ans += 1  # 没有出现偶数比它大
            break
    print(ans)
