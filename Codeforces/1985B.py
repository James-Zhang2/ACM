for _ in range(int(input())):
    n = int(input())
    ls = []
    for x in range(2, n+1):
        div = n // x
        ls.append((x * div * (div + 1)) // 2)
    print(ls.index(max(ls)) + 2)