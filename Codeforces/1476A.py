from math import ceil
for _ in range(int(input())):
    a,b = map(int,input().split())
    k = b / a
    print(ceil(k) if k >= 1 else ceil(k) + 1)