import sys
nums=list(map(int,input().strip().split()))
k=int(input())
Size=len(nums)
def SplitArray(Arr,MaxDiff,m):
    Student=1
    CurrentPages=0
    for i in Arr:
        if CurrentPages+i<=MaxDiff:
            CurrentPages+=i
        else:
            Student+=1
            CurrentPages=i
            if Student > m:
                return Student
    return Student
if Size<k:
    print(-1)
    sys.exit()
else:
    MAxValue=-sys.maxsize
    TotalSum=0
    for i in nums:
        if i>=MAxValue:
            MAxValue=i
        TotalSum+=i
    left=MAxValue
    right=TotalSum
    while left<=right:
        mid=(left+right)//2
        Temp=SplitArray(nums,mid,k)
        if Temp>k:
            left=mid+1
        else:
            right=mid-1
    print(left)
    sys.exit()

# this is similar or same as book allocation

