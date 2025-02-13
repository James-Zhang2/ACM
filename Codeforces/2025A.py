for _ in range(int(input())):
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    n = min(len_s, len_t)
    time = len_s + len_t
    cnt = 0
    for i in range(n):
        if s[i] == t[i]:
            cnt += 1
        else:
            break
    time -= 0 if cnt == 0 else (cnt - 1)
    print(time)
# 两个指针
