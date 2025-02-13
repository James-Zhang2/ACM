for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    cnt = 0
    mx = 0
    s = 0
    for i in ls:
        s += i
        mx = max(mx, i)
        cnt += (s - mx == mx)  # 总和减剩下的值等于 i
    print(cnt)
