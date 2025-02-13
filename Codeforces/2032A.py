t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    cnt = ls.count(1)
    small = cnt % 2
    big = cnt if cnt <= n else 2 * n - cnt
    print(f"{small} {big}")
# 贪心
