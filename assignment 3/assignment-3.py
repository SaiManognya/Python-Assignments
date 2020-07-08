#1) Area of triangle
a=float(input("Enter first side of the triangle: "))
b=float(input("Enter second side of the triangle: "))
c=float(input("Enter third side of the triangle: "))
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle: ",area)

#2) String - palindrome
s=input("Enter a string: ")
c=s[::-1]
if(s==c):
    print("{} is a palindrome".format(s))
else:
    print("{} is not a palindrome".format(s))

#3) To check whether a year is leap year or not
y=int(input("Enter a year: "))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("{} is a leap year".format(y))
        else:
            print("{} is not a leap year".format(y))
    else:
        print("{} is a leap year".format(y))
else:
    print("{} is not a leap year".format(y))

#4) Replace spaces with hyphens
s=input("Enter a string: ")
c=s.replace(" ","-")
print(c)

#5) Unique sort
s = input("Enter a string: ")
def alphasort(s):
    c=s.split(',')
    b=set(c)
    c=list(b)
    c.sort()
    s=','.join(c)
    return s
print(alphasort(s))

#6) Tax calculator
salary=int(input("Enter monthly salary: "))
if(salary<=250000):
    print("Tax is Nill")
elif(salary<=500000):
    print("Tax is 5 percent")
elif(salary<=750000):
    print("Tax is 10 percent")
elif(salary<=1000000):
    print("Tax is 15 percent")
elif(salary<=1250000):
    print("Tax is 20 percent")
elif(salary<=1500000):
    print("Tax is 25 percent")
else:
    print("Tax is 30 percent")

#7) Converting arguments into a single integer
l=[11, 33, 50]
for i in l:
    print(i,end = "")

#8) no.of seconds
d=int(input("Enter no.of days: "))
ds=d*24*60*60
h=int(input("Enter no.of hours:"))
hs=h*60*60
m=int(input("Enter no.of minutes:"))
ms=m*60
s=int(input("Enter no.of seconds:"))
ts=ds+hs+ms+s
print("Total no.of seconds: ",ts)

#9) Sort 3 integers
a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))
c=int(input("Enter third integer: "))
d=[a,b,c]
m=max(a,b,c)
n=min(a,b,c)
x=d[0]+d[1]+d[2]-m-n
print(n,x,m)

#10) successor of the date
y=int(input("Enter a year: "))
if(y%4==0):
    leapyear=True
elif(y%100==0):
    leapyear=False
elif(y%400==0):
    leapyear=True
else:
    leapyear=False
m=int(input("Enter a month [1-12]: "))
if m in (1,3,5,7,8,10,12):
    ml=31
elif m==2:
    if leapyear:
        ml=29
    else:
        ml=28
else:
    ml=30
d=int(input("Enter a day: "))
if d < ml:
    d=d+1
else:
    d=1
    if m==12:
        m=1
        y=y+1
    else:
        m=m+1
print("The successor of the date is %d-%d-%d "%(y, m, d))

#11) product of list
l=[45,3,2,89,72,1,10,7]
def product(l):
    p=1
    for i in l:
        p=p*i
    return(p)
print(product(l))

#12)
def Num_list(a,b,c,d,e,f):
    return(a+b,b+c,c+d,d+e,e+f)
c=Num_list(5,6,8,34,89,1)
print(c)

#13)
def Num_tuple(a,b,c,d,e,f):
    return(a,a*b,a*b*c,a*b*c*d,a*b*c*d*e,a*b*c*d*e*f)
d=Num_tuple(5,6,8,3,9,1)
print(d)

#14)
num=int(input("Enter a number:"))
elist=[]
x=0
while num>0:
    y=num%10
    num=num//10
    x=x*10+y

while x>0:
    y=x%10
    x=x//10
    elist.append(y)
print(elist)

#15) largest palindrome in substring
s=input("Enter a palindrome: ")
def palindrome(s):
    p1=1
    p2=0
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if s[i:j]==s[j:i:-1]:
                if len(s[i:j]) > p1:
                    p1=len(s[i:j])
                    ps=(s[i:j+1])
                    p2=1
    if p2:
        return(ps)
    else:
        return('No palindrome')
print(palindrome(s))

#16) Substring Check
x=input("Enter binary string of length 5:")
y=input("Enter binary string of length 10:")
if x[:] in y[:] :
    print(1)
else:
    print(0)

#17) No.of steps
def watersteps(a,b,c):
    va=a
    vb=0
    j=1
    while va!=c and vb!=c:
        if vb == b:
            vb = 0
            j=j+1
        elif va == 0:
            va = a
            j=j+1
        else:
            x=min(a,b)
            va=va-x
            vb=vb+x
            j=j+1
    return j
t=int(input("Enter no.of test cases: "))
for i in range(t):
    a=int(input("Enter a litres:"))
    b=int(input("Enter b litres:"))
    c=int(input("Enter c litres:"))
    if (c>max(a,b)):
        print(-1)
    else:
        s=watersteps(a,b,c)
        print(s)




