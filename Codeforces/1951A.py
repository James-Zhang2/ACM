for _ in range(int(input())):
    n = int(input())
    a = input()
    s = a.count('1')
    if s % 2 or ('11' in a and s == 2):
        print("NO")
    else:
        print("YES")