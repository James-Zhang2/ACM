for _ in range(int(input())):
    s,i=list(map(int,input())),1
    while i<len(s):
        if i>0 and s[i]>s[i-1]+1:
            s[i],s[i-1],i=s[i-1],s[i]-1,i-1  # 这里很巧妙，如129，第一步先不动，第二步变为182，再回退检查1和8-1的大小关系，变为712
        else:
            i+=1
    print(*s,sep="")