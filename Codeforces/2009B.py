for _ in range(int(input())):
    n = int(input())
    print(*[input().index('#') + 1 for _ in range(n)][::-1])
