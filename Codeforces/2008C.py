from bisect import bisect_left as bi


for _ in range(int(input())):
    l, r = map(int, input().split())
    diff = r - l
    check = lambda k: k * (k + 1) // 2 > diff  # 注意：写二分如果要套模板要保证左侧都是False，右侧都为True，如果发现结果不对可以将自变量 +1 or -1
    print(bi(range(diff + 1), True, 1, key=check))
