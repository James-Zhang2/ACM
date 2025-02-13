n, m, k = map(int, input().split())
ls = [10 ** 6] * m
for _ in range(n):
    r, c = map(int, input().split())
    ls[r-1] = min(ls[r-1], c)
print(min(sum(ls), k))
