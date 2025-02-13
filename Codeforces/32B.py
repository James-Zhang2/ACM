s = input()
n = len(s)
cur = 0
ans = ""
while cur < n:
    if s[cur] == ".":
        ans += "0"
        cur += 1
    else:
        if s[cur+1] == ".":
            ans += "1"
        else:
            ans += "2"
        cur += 2
print(ans)