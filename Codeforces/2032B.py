for t in range(int(input())):
    n, k = map(int, input().split())
    if n == 1:
        print(1)
        print(1)
    elif k == 1 or k == n:
        print(-1)
    elif k % 2 == 0:
        print(3)
        print(1, k, k + 1)
    else:
        print(5)
        print(1, 2, k, k + 1, k + 2)
# 此问题还未完全理解，类似构造问题
