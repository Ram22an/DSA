import sys
nums=list(map(int,input().strip().split()))
nums.sort()
Size=len(nums)
if Size==1:
    print(nums[0])
if nums[0]!=nums[1]:
    print(nums[0])
if nums[-1]!=nums[-2]:
    print(nums[-1])
right=Size-2
left=1
Ans=sys.maxsize
while left<=right:
    mid=(left+right)//2
    if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
        Ans=mid
        break
    if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid+1]==nums[mid]):
        left=mid+1
    else:
        right=mid-1
print(nums[Ans])
# i didn't got the logic i will get it later
