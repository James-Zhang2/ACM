from collections import Counter as cnt
for _ in range(int(input())):
    n, x = map(int, input().split())
    c = cnt(map(int, input().split()))  # 不用害怕，Counter (cnt) 会产生 一个 记录 每个数字 出现次数 的 列表
    z = 0
    while c[z]:  # 确保 z 的 出现次数 大于 0，这里的 z 相当于 指针 cur
        c[z + x] += c[z] - 1  # c[z] = 1 时，后面 元素 不增加，往后推 x 时 由于 被使用 一次 消耗 1
        z += 1
    print(z)
