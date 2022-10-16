# Built in fuction
a = 9
b = 10
c = sum((a,b))
print(c)

# User Defined Fuctions
def greet():
    print("Hello Sir how are you!")

def greetwithname(name):
    print("Hello ",name," how are you!")

greetwithname("Sahil")

def avg(a,b):
    sum = a + b
    average = sum/2
    print("Average of",a,"and",b,"is =",average)

avg(25,50)
avg(20,10)
avg(65,20)