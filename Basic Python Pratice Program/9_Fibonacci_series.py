# Fibonacci Series
import math


# Fibonacci Series Using space optimised method
def fibSeries(n):
    a = 0
    b = 1
    print("Fibonacci Series using space optimised Method")
    if n < 0:
        print("Incorrect Input!")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        print(a)
        print(b)
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(b)
    print("\nFibonacci series using recursion method")
    for i in range(0, n + 1):
        print(fibRecursion(i))
    print("\nFibonacci series using direct formula method")
    for i in range(0, n + 1):
        print(fibFormula(i))


# Fibonacci number using recursion
def fibRecursion(n):
    if n < 2:
        return n
    return fibRecursion(n - 1) + fibRecursion(n - 2)


# Fibonacci Number using formula
def fibFormula(n):
    return int(((math.pow(((1 + math.sqrt(5)) / 2), n)) - (math.pow(((1 - math.sqrt(5)) / 2), n))) / math.sqrt(5))


n = int(input("Enter a Number->"))
fibSeries(n)
