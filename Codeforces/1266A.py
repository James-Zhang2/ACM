for _ in range(int(input())):
    n = input()
    ls = [int(i) % 2 for i in n]
    digits = 0
    for j in n:
        digits += int(j)
    cnt = ls.count(0)
    print("red" if digits % 3 == 0 and cnt >= 2 and "0" in n else "cyan")
# 中国剩余定理，被2和30整除即被60整除
