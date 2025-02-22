# https://ac.nowcoder.com/acm/contest/90072/D
check=lambda x:(x**0.5)%1==0
n,m=map(int,input().split())
ls=list(map(int,input().split()))
c=[0]*(n+1)
for i in range(n):
    res = 0
    for j in range(i, n):
        res += ls[j]
        if check(res):
            c[i] += 1
            c[j+1] -= 1
for i in range(n-1):c[i+1] += c[i]
for _ in range(m):
    a = int(input())
    print(c[a-1])
