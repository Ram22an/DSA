import math
def CanEatInRange(arr,time,ActualTime):
    TotalTime=0
    for i in arr:
        TotalTime+=math.ceil(i/time)
    if TotalTime<=ActualTime:
        return True
    else:
        return False
piles=list(map(int,input().strip().split()))
h=int(input())
left=1
right=max(piles)
Ans=0
while left<=right:
    mid=(left+right)//2
    Temp=CanEatInRange(piles,mid,h)
    if Temp:
        Ans=mid
        right=mid-1
    else:
        left=mid+1
print(Ans)
