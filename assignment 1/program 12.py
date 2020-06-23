#(a)
num1,num2 = "94","30"
data = "As per Census 2011, Gender ratio of India is 943 females per 1000 males"
num1+num2[0] in data
print(num1+num2[0] in data)
'''From the given data num1 is 94 and num2[0] is 3 from the print statement num1+num2[0] is a concatenation operator
which results in 943 and 943 in data is a membership operator as 943 is present in the data it prints True '''
#(b)
print(data[:45],print(int(num1)+int(num2)))
'''At first it convers num1,num2 to int then it will be added
then using slicing [:45] it stops at 44th position and prints as 
As per Census 2011, Gender ratio of India is
as there is no return value for print(int(num1)+int(num2)) it prints None'''