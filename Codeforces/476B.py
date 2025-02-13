from math import comb
a = input()
b = input()
ans = a.count("+") - a.count("-")
pre = b.count("+") - b.count("-")
dif = abs(ans - pre)
num = b.count("?")
if not num:
    if ans == pre:
        print(float(1))
    else:
        print(float(0))
else:
    if dif > num:
        print(float(0))
    else:
        c = dif + (num - dif) // 2
        print(0.5 ** num * comb(num, c))
