for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    m = max(ls) + 1  # 此时m是最佳状态
    for i in range(n - 2):
        ls[i + 1] += ls[i]
    ls = [0] + ls
    print(*[i + m for i in ls])
