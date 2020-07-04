num=int(input("Enter an integer: "))
if(100<num<1000):
    s=0
    while num>0:
        r=num%10
        s=s+r
        num=num//10
print(s)