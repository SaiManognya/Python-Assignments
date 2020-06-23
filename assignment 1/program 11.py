msg2 = "welcome to sr engineering college"
x = msg2.count("o")
y = msg2.count("r")
C=msg2[y**x:(x**y+x+y):][::-1]
print(C)
'''In x we had written the occurence of o through count() function i.e. 3 and in y we had written the
occurence of r through the same count() function i.e. 2 then the value of variable C goes with 
[y**x:(x**y+x+y):][::-1] as [2**3:(3**2+3+2):][::-1] as [8:14:][::-1] 
here it starts from index 8 and stops at 13th index then using [::-1] it will reverse the value'''