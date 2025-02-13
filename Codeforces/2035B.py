t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1 or n == 3:
        print(-1)
        continue
    elif n % 2:
        print(int((n - 4) * "3" + "6366"))
    else:
        print(int((n - 2) * "3" + "66"))
