for i in range(1,1001):
    m=i
    s=0
    while i>0:
        r=i%10
        s=s*10+r
        i=i//10
    if(s==m):
        print(s)