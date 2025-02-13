for _ in range(int(input())):
    n, r = map(int, input().split())
    ls = list(map(int, input().split()))
    happy = left = 0
    for i in ls:
        happy += (i // 2) * 2
        r -= i // 2
        left += i & 1

    """
    这段代码很像贪心的分段函数：x 和 2n - x
    """
    if left > r:
        happy += 2 * r - left
    else:
        happy += left
    print(happy)