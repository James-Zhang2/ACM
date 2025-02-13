for _ in range(int(input())):
    n,m,r,c = map(int, input().split())
    move = n * m - ((r - 1) * m + c)
    print((n - r) * m + (move - n + r))