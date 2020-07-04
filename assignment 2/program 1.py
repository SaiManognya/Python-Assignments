year=int(input("Enter year: "))
c= year%12
if(c==0):
    print("monkey")
elif(c==1):
    print("rooster")
elif(c==2):
    print("dog")
elif(c==3):
    print("pig")
elif(c==4):
    print("rat")
elif(c==5):
    print("ox")
elif(c==6):
    print("tiger")
elif(c==7):
    print("rabbit")
elif(c==8):
    print("dragon")
elif(c==9):
    print("snake")
elif(c==10):
    print("horse")
else:
    print("sheep")