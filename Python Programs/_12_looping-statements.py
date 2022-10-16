# We will run a loop in which multiple times a statement will execute

# for, while

newlist = ["Sahil","Batra","Infotech","Programmer"]

for element in newlist:
    print(element)

    
newlist1 = [["My Name", "Sahil","Batra"],["Channel Name", "Infotech","Programmer"]]

for item in newlist1:
    print(item)

newlist2 = [["Sahil",20],["John",25],["Shawn",36]]

for name,age in newlist2:
    print(name," age is ",age)

num = 1

while(num<=5):
    print(num)
    num = num + 1 