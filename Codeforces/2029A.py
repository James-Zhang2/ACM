t = int(input())
for _ in range(t):
    l, r, k = map(int, input().split())
    if r < k * l:
        print(0)
        continue
    else:
        print(int((r - k * l) / k) + 1)
