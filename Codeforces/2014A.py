for _ in range(int(input())):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    gold = 0
    cnt = 0
    for i in ls:
        if i >= k: gold += i
        if i == 0 and gold > 0: gold -= 1; cnt += 1
    print(cnt)
