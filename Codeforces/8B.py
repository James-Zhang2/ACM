def solve():
    d = {}
    d4 = (1, 0), (0, 1), (-1, 0), (0, -1)
    for i, item in enumerate('RULD'):
        d[item] = d4[i]
    path = input()
    x, y = 0, 0
    visited = set()
    for item in path:
        i, j = d[item]
        prev = x, y
        x += i
        y += j
        for i, j in d4:
            if (x + i, y + j) in visited:
                print('BUG')
                return
        visited.add(prev)
    print('OK')

solve()