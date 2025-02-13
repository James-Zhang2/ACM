a, b, x, y = map(int, input().split())
a = max(a,b)
b = min(a,b)
x = max(x,y)
y = min(x,y)
if a * y > b * x:
    a_1 = b * x / y
    print(f"{int(a_1)} {b}" if int(a_1) == a_1 else "0 0")
else:
    b_1 = a * y / x
    print(f"{a} {int(b_1)}" if int(b_1) == b_1 else "0 0")
