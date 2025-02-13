n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
w = 0
for i in ls[0:m]:
    if i >= 0:
        break
    else:
        w -= i
print(w)
# 贪心
