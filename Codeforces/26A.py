n = int(input())
l = [0] * (n + 1)
for i in range(2, n + 1):
    if l[i] == 0:  # 是质数
        for j in range(2 * i, n + 1, i):  # 质数的倍数
            l[j] += 1
print(l.count(2))
# 这个代码极为精妙，有筛法求质数的思想，值得好好研究
