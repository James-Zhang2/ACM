s = input()
t = input()
a = s[0]
b = t[-1]
s = s[1:]
t = t[:-1]
t = t[-1::-1]
x = len(t)
res = -1
m = 1000000
for c in 'qwertyuiopasdfghjklzxcvbnm':
    if c in s and c in t:
        i1 = s.index(c)
        i2 = t.index(c)
        ans = a+s[:i1]+t[i2::-1]+b
        l = len(ans)
        if l < m:
            res = ans
            m = l
print(res)
# 一种很好的处理字符串的方法（遍历键盘）
