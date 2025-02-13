t = int(input())
for _ in range(t):
    la, ra = map(int, input().split())
    lb, rb = map(int, input().split())
    lx = max(la, lb)
    rn = min(ra, rb)
    if lx > rn:
        print(1)
    else:
        if la == lb and ra == rb:
            print(rn - lx)
        elif la == lb or ra == rb:
            print(rn - lx + 1)
        else:
            print(rn - lx + 2)
