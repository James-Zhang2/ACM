# https://codeforces.com/contest/19/problem/A

n = int(input())
a = dict()
for _ in range(n):
    a[input()] = [0] * 4

for _ in range((n * (n - 1)) // 2):
    s1, s2 = input().split()
    b, c = s1.split("-")
    b1, c1 = map(int, s2.split(":"))

    if b1 > c1: a[b][0] += 3
    elif b1 < c1: a[c][0] += 3
    else: a[b][0] += 1;a[c][0] += 1

    a[b][1] += (b1 - c1);a[c][1] += (c1 - b1)
    a[b][2] += b1;a[b][3] += c1
    a[c][2] += c1;a[c][3] += b1

a = list(a.items())
a.sort(reverse=True, key=lambda i: i[1])

a = [i[0] for i in a[:n//2]]
a.sort()

for i in a: print(i)
