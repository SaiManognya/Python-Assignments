w=int(input("Enter weight in pounds: "))
h=int(input("Enter height in inches: "))
wtkg=float(w*0.45359237)
htm=float(h*0.0254)
bmi=float(wtkg/htm**2)
if(bmi<18.5):
    print("Underweight")
elif(18.5<=bmi<25.0):
    print("Normal")
elif(25.0<=bmi<30.0):
    print("Overweight")
else:
    print("Obese")