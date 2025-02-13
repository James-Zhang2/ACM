for _ in range(int(input())):
    n, m = map(int, input().split())
    l = 0
    cnt = 0
    for i in range(n):
        l += len(input())
        if l <= m:
            cnt += 1
        else:
            break
    print(cnt)