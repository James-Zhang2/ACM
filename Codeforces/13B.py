from math import gcd
a = int(input())
r = 0
for b in range(2, a):
    c = a
    while c:
        r += c % b
        c //= b
a -= 2
d = gcd(r, a)           # 输入r, a 可以求出最简分式 p/q
print(f'{r//d}/{a//d}')
