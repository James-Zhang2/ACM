from math import sqrt
x = int(input())
x = abs(x)

a = (sqrt(1 + 8 * x) - 1) // 2

if (1 + a) * a / 2 == x:
    print(int(a))
elif ((1 + a) * a / 2 + a + 1 - x) % 2 == 0:
    print(int(a + 1))
elif (a + 2) % 2 != 0:
    print(int(a + 2))
else:
    print(int(a + 3))
