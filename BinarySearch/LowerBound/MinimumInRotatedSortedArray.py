# in this i have learned one thing that try to observe the
# question and try to build the intuition
# the one thing i learned is that in rotated sorted order
# the minimum value of the array is not in the sorted part
# so when do mid=(0+n-1)//2 so it divide the array into two parts that is
# low to mide and mid+1 to high so if low<=mid then sorted or mid<=high then sorted
# so we have to search for the minimum value in the unsorted part so eleminate the sorted part
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
print(Ans)
