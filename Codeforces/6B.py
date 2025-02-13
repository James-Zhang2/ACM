from bisect import bisect_left as bi
from math import ceil
for i in range(int(input())):
    n, p, l, t = map(int, input().split())
    check = lambda k: t * min(ceil(n / 7), 2 * k) + k * l >= p
    print(n - bi(range(n + 1), True, key=check))