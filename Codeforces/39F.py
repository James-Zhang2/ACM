n, m, k = map(int, input().split())
d = list(map(int, input().split()))
i = list(map(int, input().split()))
ls = []
for a, b in enumerate(d, 1):
    cnt = 0
    for c in i:
        if c % b == 0:
            cnt += 1
    ls.append((a, cnt))
ls.sort(key=lambda x: x[1])
num = ls[0][1]
cnt = 0
e = []
for j in range(m):
    if ls[j][1] == num:
        cnt += 1
        e.append(ls[j][0])
    else:
        break
print(cnt)
print(*e)
