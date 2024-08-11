def Fibonacci(x):
    if x <= 1:
        return x
    return Fibonacci(x - 1) + Fibonacci(x - 2)

x = int(input())
print(Fibonacci(x))
