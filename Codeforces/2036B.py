t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = dict()
    for i in range(k):
        b, c = map(int, input().split())
        a[b] = c + a.get(b, 0)
    ls = list(a.values())
    ls.sort(reverse=True)
    print(sum(ls) if n >= k else ls[0:n])
# 学会元组后用元组加lambda i: i[1]来排序
# 贪心
