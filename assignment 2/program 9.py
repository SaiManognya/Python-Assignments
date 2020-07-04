for i in range(1,1001):
    s=0
    m=i
    while i>0:
        r=i%10
        s=s+r*r*r
        i=i//10
    if(s==m):
        print(m)