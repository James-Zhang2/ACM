t = int(input())
for _ in range(t):
    n = int(input())

    q = int(input())
    a = list(map(int, input().split()))
    for k in range(q - 2):
        if a[k] != a[k + 1]:
            print(f"{k} {k + 1}")
    print("-1 -1")