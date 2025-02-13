for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    cnt = cur = ans = 0
    while cur < len(s):
        if s[cur] == "1":
            cnt = 0
        else:
            cnt += 1
            if cnt == m:
                ans += 1
                cur += k - 1
                cnt = 0
        cur += 1
    print(ans)