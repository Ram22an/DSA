def Factorial(x):
    if x==1:
        return 1
    return x*Factorial(x-1)
x=int(input())
print(Factorial(x))
