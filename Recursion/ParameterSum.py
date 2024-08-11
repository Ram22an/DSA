def TotalSum(x,TSum):
    if x==0:
        return TSum
    TSum+=x
    return TotalSum(x-1,TSum)
x=int(input())
TSum=0
temp=TotalSum(x,TSum)
print(temp)
