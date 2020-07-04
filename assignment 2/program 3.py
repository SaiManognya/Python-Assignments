seat=input("Type of Seat: ")
if(seat == 'Stalls'):
    rate=625
elif(seat == 'Circle'):
    rate=750
elif(seat == 'UpperClass'):
    rate=850
else:
    rate=1000
mode=input("Payment mode: ")
if(mode == 'Cash'):
    d=10/100
else:
    d=5/100
c=rate*d
print("Cost of ticket: ",int(rate-c))