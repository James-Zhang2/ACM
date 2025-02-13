from math import ceil
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    dx = ceil(x / k)
    dy = ceil(y / k)
    print(2 * ceil(max(dx, dy)) - (dx > dy))
