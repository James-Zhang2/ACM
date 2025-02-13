a, b = 0, 1
ls = [-1]
s = input()
for i, c in enumerate(s):
    if c == "(":
        ls.append(i)
    elif len(ls) > 1:
        ls.pop()
        n = i - ls[-1]
        if a < n:
            a, b = n, 1
        elif a == n:
            b += 1
    else:
        ls[0] = i
print(a, b)
