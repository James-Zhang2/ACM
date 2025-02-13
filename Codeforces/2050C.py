for _ in range(int(input())):
    n = input()
    n_9 = sum([int(k) for k in n])
    x = min(n.count("2"), 8)
    y = min(n.count("3"), 8)


    def test():
        for i in range(x+1):
            for j in range(y+1):
                if (n_9 + 2 * i + 6 * j) % 9 == 0:
                    return True
        return False


    print("YES" if test() else "NO")
