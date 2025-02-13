for _ in range(int(input())):
    n = input()
    l = filter(lambda x : x <= 2048,  map(int, input().split()))
    print('YES' if sum(l) >= 2048 else 'NO')
