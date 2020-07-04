d=int(input("Distance to be travel: "))
w=int(input("Weight of the goods: "))
if(d>=500):
    if(w>=100):
        c=5
    elif(w>=10 and w<100):
        c=6
    else:
        c=7
else:
    if(w>=100):
        c=8
    else:
        c=5
print("Amount to be charged: ",d*c)