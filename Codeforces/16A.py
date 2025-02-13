n, m = map(int, input().split())
ls = []


def test():
    for i in range(n):
        t = input()
        if t.count(t[0]) < m:
            print("NO")
            return
        else:
            ls.append(t[0])
            if i >= 1:
                if ls[i] == ls[i-1]:
                    print("NO")
                    return
    print("YES")


test()
