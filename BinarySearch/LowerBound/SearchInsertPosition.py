def searchInsert(nums: list[int], target: int) -> int:
    ans=len(nums)
    right=len(nums)-1
    left=0
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            ans=mid
            right=mid-1
        else:
            left=mid+1
            
    return ans
arr=list(map(int,input().strip().split()))
x=int(input())
print(searchInsert(arr,x))
# it is similar to the Ceil The Floor question
