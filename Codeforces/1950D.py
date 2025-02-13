spis = [10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111, 100000]
def rec(num, n):
    if num == n:
        return True
    if num > n:
        return False
    for i in spis:
        if rec(num * i, n):
            return True
    return False

for _ in range(int(input())):
    n = int(input())
    if rec(1, n):
        print("YES")
    else:
        print("NO")