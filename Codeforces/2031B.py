def test():
    for i in range(n):
        if abs(ls[i] - i - 1) > 1:  # 超出翻转半径 1，则一定不满足条件
            print('NO')
            return
    print('YES')


for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    sg = False
    test()
# 贪心
