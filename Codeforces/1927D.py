# import sys
# from random import randint, shuffle, choice
# from math import gcd, lcm, sqrt, isqrt, perm, comb, factorial, log2, ceil, floor
# from collections import Counter, defaultdict, deque
# from functools import lru_cache, reduce, cmp_to_key
# from itertools import accumulate, combinations, permutations, product, repeat, takewhile, starmap, dropwhile, cycle
# from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush, _heapify_max
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from operator import sub , mul,pow  , truediv , floordiv
# input = lambda: sys.stdin.buffer.readline().decode().rstrip()
# OneByOne = lambda: sys.stdin.read(1)

I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
yes = lambda: print('YES')
no = lambda: print('NO')
DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
MOD = 10 ** 9 + 7
inf = float('inf')

# 高级算法，目前不懂
for _ in range(II()):
    n = II()
    a = LII()

    ans = [0] * n
    ans[-1] = n
    for i in range(n - 2, -1, -1):
        ans[i] = i + 1 if a[i] != a[i + 1] else ans[i + 1]

    for __ in range(II()):
        l, r = MII()
        print(*(l, ans[l - 1] + 1) if ans[l - 1] < r else (-1, -1))
    print()