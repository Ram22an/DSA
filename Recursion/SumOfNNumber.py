# this is without parameter
def SumOfN(n):
    if n==1:
        return 1
    return n+SumOfN(n-1)
x=int(input())
temp=SumOfN(x)
print(temp)
