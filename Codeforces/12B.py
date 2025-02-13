n = input()
m = input()
ls = []
mystr = ""
for i in n:
    num = int(i)
    if num:
        ls.append(num)
        ls.sort()
cnt = n.count("0")
if cnt:
    for _ in range(cnt):
        ls.insert(1, "0")
for j in ls:
    mystr += str(j)
print("OK" if mystr == m else "WRONG_ANSWER")
