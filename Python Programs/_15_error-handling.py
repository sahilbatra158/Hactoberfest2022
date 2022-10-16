# try and except concept for error handling (runtime error/exception handling)
try:
    print("Enter number-1")
    num1 = int(input())
    print("Enter number-2")
    num2 = int(input())
    sum = num1 + num2
    print(sum)
except:
    print("Value entered is wrong")


print("Above is the sum of two numbers")