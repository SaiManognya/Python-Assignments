msg2 = "welcome to sr engineering college"
x = msg2.count("o")
y = msg2.count("r")
C=msg2[y**x:(x**y+x+y):][::-1]
print(C)