n = int(input())
ls = list(map(int, input().split()))
odd = 0
for i in range(3):
    odd += 1 if ls[i] % 2 else 0
if odd >= 2:
    for j in ls:
        if j % 2 == 0:
            print(ls.index(j) + 1)
else:
    for j in ls:
        if j % 2:
            print(ls.index(j) + 1)
