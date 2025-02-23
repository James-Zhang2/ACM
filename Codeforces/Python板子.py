from math import sqrt,ceil,gcd;import sys;sys.setrecursionlimit(1000000);input=lambda:sys.stdin.readline().strip();re=lambda:map(int,input().split())


# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
# from collections import deque,Counter
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import ceil,floor,inf,sqrt,gcd,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate

MOD=int(1e9+7)
dot_product=lambda m,n:sum(m[i]*n[i] for i in range(3))
cross_product=lambda m,n:[m[1]*n[2]-m[2]*n[1],m[2]*n[0]-m[0]*n[2],m[0]*n[1]-m[1]*n[0]]
module=lambda x:sqrt(sum(i**2 for i in range(3)))
vectify=lambda a,b:[a[i]-b[i] for i in range(3)]
mod_inv=lambda a,mod:pow(a,mod-2,mod)
sum_range=lambda p,q: (q - p + 1) * (p + q) // 2
sum_squares=lambda p,q: (q * (q + 1) * (2 * q + 1) - (p - 1) * p * (2 * p - 1)) // 6
py=lambda:print("YES")
pn=lambda:print("NO")
