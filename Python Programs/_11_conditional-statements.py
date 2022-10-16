# if-else

var1 = 30
var2 = 30 

if var1 < var2:
   print(var1," is smaller") 
else:
    print(var2," is smaller")

# Multiple conditions

if var1 > var2:
    print(var1," is greater")
elif var2 > var1:
    print(var2," is greater")
else:
    print("Both are equal")

newlist = [2,3,4,15,7]

if 5 in newlist:
    print("Yes")
else:
    print("No")


a = 25
b = 35

# if a>b: print("A is big")

print("A is Big") if a>b else print("B is big")