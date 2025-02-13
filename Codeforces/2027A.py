for _ in range(int(input())):
    wmax = 0
    hmax = 0
    for __ in range(int(input())):
        wi, hi = map(int, input().split())
        wmax = wi if wi > wmax else wmax
        hmax = hi if hi > hmax else hmax
    print(2 * (wmax + hmax))
