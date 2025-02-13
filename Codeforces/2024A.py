for _ in range(int(input())):
    a, b = map(int, input().split())
    if a >= b:
        print(a)
    else:
        c = 2 * a - b
        print(c if c >= 0 else 0)
