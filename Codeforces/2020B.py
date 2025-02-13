from math import isqrt
for _ in range(int(input())):
    n = int(input())
    print(n + isqrt(n + isqrt(n)))
