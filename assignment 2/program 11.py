h=int(input('Enter height of the well: '))
u=int(input('distance-climbs up: '))
d=int(input('distance-slips down: '))
n=int((h-u)/(u-d))
print(int(n+2))

#another method#

'''h=int(input('Enter height of the well: '))
u=int(input('distance-climbs up: '))
d=int(input('distance-slips down: '))
x=0
for i in range(1,h**2):
    c=u-d
    x=x+c
    if(x>h):
        print(i)
        break
    elif(x==h):
        if(i%2==0):
            print(i-2)
            break
        else:
            print(i-1)
            break'''
