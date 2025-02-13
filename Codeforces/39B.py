n = int(input())
ls = list(map(int, input().split()))
cur = 1
ans = []
for i in range(n):
    if ls[i] == cur:
        ans.append(2001 + i)
        cur += 1
cur -= 1
print(cur)
print(*ans)