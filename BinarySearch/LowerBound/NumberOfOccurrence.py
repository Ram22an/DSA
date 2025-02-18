nums=list(map(int,input().strip().split()))
target=int(input())
if not nums:
    print(0)
if len(nums)==1 and nums[0]==target:
    print(0)
ansUpperBound=-1
right=len(nums)-1
left=0
while left<=right:
    mid=(left+right)//2
    if nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
ansUpperBound=left-1
ansLowerBound=-1
right=len(nums)-1
left=0
while left<=right:
    mid=(left+right)//2
    if nums[mid]>=target:
        ansLowerBound=mid
        right=mid-1
    else:
        left=mid+1
if ansLowerBound==len(nums) or nums[ansLowerBound]!=target:
    print(0)
else:
    print(ansUpperBound-ansLowerBound+1)
# it is similar to Find First And Last Position Of Element In Sorted Array
# the only difference is that the print(ansUpperBound-ansLowerBound+1)
