for _ in range(int(input())):
    s = input()
    n = len(s)
    k = s.find('0')
    if k == -1:
        print(1, n, n, n)
    else:
        l = n - k
        p = s[k:].find('1')
        if p == -1:
            k = 0
        else:
            k = max(k - p, 0)  # 此处是需要移动到的索引位置，实际含义就是让 1 尽可能的和 0 异或，但不要超出范围，影响到后面的 1（这样会变小）
        print(1, n, k + 1, k + l)
