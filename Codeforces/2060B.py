import sys;input=lambda:sys.stdin.readline().strip();re=lambda:map(int,input().split())
t,=re()
for _ in range(t):
    n,m=re()
    ans=[0]*n
    bl=True
    for i in range(1,n+1):
        a=list(re())
        if bl:x=a[0]%n;bl=all(i%n==x for i in a);ans[x]=i  # bl为True再进行判断，为False只进行读入操作
    if bl:print(*ans)
    else:print(-1)