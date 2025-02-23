import math
nums=list(map(int,input().strip().split()))
threshold=int(input())
left=1
right=max(nums)
Ans=0
while left<=right:
    mid=(left+right)//2
    TempAdd=0
    for i in nums:
        TempAdd+=math.ceil(i/mid)
    if TempAdd<=threshold:
        Ans=mid
        right=mid-1
    else:
        left=mid+1
print(Ans)
