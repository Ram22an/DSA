import sys
nums=list(map(int,input().strip().split()))
Ans=sys.maxsize
left=0
right=len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]>=nums[left]:
        Ans=min(nums[left],Ans)
        left=mid+1
    else:
        Ans=min(nums[mid],Ans)
        right=mid-1
print(nums.index(Ans))
# it is similar to the Minimum In Rotated Sorted Array
# the only difference is that we have to return the index of the smallest element
