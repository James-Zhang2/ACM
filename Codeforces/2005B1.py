def solve():
    n, m, q = map(int, input().split())
    b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in a:
        if i < b[0]:
            print(b[0] - 1)
        elif i > b[-1]:
            print(n - b[-1])
        else:
            print((b[-1] - b[0]) // 2)


for _ in range(int(input())):
    solve()
