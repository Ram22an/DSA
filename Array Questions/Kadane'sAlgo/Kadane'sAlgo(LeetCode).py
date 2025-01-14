# this is used to find sub array with maximum sum
# first approach include 3 loops which lead to O(n^3)
TotalSum=0
arr=list(map(int,input().strip().split()))
MaxSum=arr[0]
for i in range(0,len(arr)):
    TotalSum+=arr[i]
    if MaxSum<TotalSum:
        MaxSum=TotalSum
    if TotalSum<0:
        TotalSum=0
print(MaxSum)
