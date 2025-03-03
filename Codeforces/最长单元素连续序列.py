# https://codeforces.com/contest/2064/problem/B
# this is a two pointers problem
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = [0] * n
    r = [0, 0]
    diff, l = 0, 0
    for i in a:
        m[i - 1] += 1
    for i in range(n):
        if m[a[i] - 1] != 1:
            l = i + 1
        elif diff < i - l + 1:  # update when new distance is bigger than the older one
            diff = i - l + 1
            r = [l, i]
    if diff:
        print(r[0] + 1, r[1] + 1)
    else:
        print(0)
