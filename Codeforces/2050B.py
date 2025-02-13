for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    odd = n // 2
    even = n - odd
    sa = sum([ls[2 * i + 1] for i in range(odd)])
    sb = sum([ls[2 * j] for j in range(even)])
    print("YES" if (sa / odd == sb / even == sa // odd) else "NO")
