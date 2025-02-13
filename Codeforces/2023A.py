for _ in range(int(input())):
    n = int(input())
    ls = [tuple(map(int, input().split())) for __ in range(n)]
    ls.sort(key=lambda i: i[0] + i[1])
    for j in ls:
        print(*j, end=" ")
    print()