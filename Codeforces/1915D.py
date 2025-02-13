for i in range(int(input())):
    n = int(input())
    s = [str(j) for j in input()]  # 遍历每个字母并存入列表
    for j in range(2, n):
        if s[j] in 'ae':
            s[j-1] = '.' + s[j-1]
    print(''.join(s))
# 字符串处理的好题目
