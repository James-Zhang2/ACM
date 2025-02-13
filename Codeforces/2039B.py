def solve():
    s = input()
    n = len(s)
    if n == 1:
        print(-1)
        return
    elif n == 2:
        print(s if s[0] == s[1] else -1)
        return
    else:
        for i in range(n - 2):
            a, b, c = s[i], s[i + 1], s[i + 2]
            if a != b and a != c and b != c:
                print(s[i:i + 3])
                return
        for i in range(n - 1):
            a, b = s[i], s[i + 1]
            if a == b:
                print(s[i:i + 2])
                return
            print(-1)


for _ in range(int(input())):
    solve()