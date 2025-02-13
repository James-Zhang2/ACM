for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    score = (n - 1) * (max(a) - min(a))
    print(score)
