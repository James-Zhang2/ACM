for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    for i in range(n):
        if a[x] <= b[i]:
            x += 1
    print(n - x)
# 两个指针的问题都需要一定的思维能力
