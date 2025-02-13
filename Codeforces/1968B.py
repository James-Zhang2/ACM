for _ in range(int(input())):
    input()
    a = input()
    b = input()
    res = 0
    for bi in b:
        if bi == a[res]:
            res += 1  # 子序列经常用的方法，满足条件后指针移动 1。
            if res == len(a):
                break
    print(res)
# 两个指针
