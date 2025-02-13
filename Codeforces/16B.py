n, m = map(int, input().split())
s, t = 0, [tuple(map(int, input().split())) for i in range(m)]
t.sort(reverse=True, key=lambda i: i[1])  # 需要传入一个函数，根据函数大小f(i)比较大小
for i in t:
    s += i[0] * i[1]
    n -= i[0]
    if n < 0:
        s += i[1] * n  # 用 while n < 0:又增加一个循环。贪心算法需要遍历列表，直接用for i in ls: if ...
        break
print(s)
