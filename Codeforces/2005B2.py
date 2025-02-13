from bisect import bisect_left as bi


def solve():
    n, m, q = map(int, input().split())
    b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b.sort()
    for i in a:
        idx = bi(b, i)
        if idx == 0:
            print(b[0] - 1)
        elif idx == m:
            print(n - b[-1])
        else:
            print((b[idx] - b[idx - 1]) >> 1)


for _ in range(int(input())):
    solve()
