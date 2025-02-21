# peak element is nums[n-1]<nums[n]>nums[n+1]
nums=list(map(int,input().strip().split()))
# my first approach is to return the max element
# and my second approach is to do this
# Ans=0
# Size=len(nums)
# if Size>1:
#     if nums[0]>nums[1]:
#         Ans=nums[0]
# for i in range(1,Size):
#     if i<Size-2 and nums[i-1]<nums[i] and nums[i]>nums[i+1]:
#         Ans=nums[i]
#     else:
#         if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
#             Ans=nums[i]
# print(Ans)
# but is was taking O(N) time


# here is the optimized approach
Size=len(nums)
if Size==0:
    print([])
if Size==1:
    print(nums[0])
if nums[0]>nums[1]:
     print(0)
if nums[-1]>nums[-2]:
     print(Size-1)
Ans=0
left=1
right=Size-2
while left<=right:
    mid=(left+right)//2
    if nums[mid]>nums[mid-1]:
        left=mid+1
    # if nums[mid]>nums[mid+1]:
    # why i have commented this because it is causing one problem example [1,2,1,2,1]
    # here mid will be 1 the middle one if i add the above statement then no condition will 
    # satisfied so it will go in infinite loop 
    # this condition arrive because mid stuck in between two peak so we have to move one side
    # why ignoring other side because in search we will find the second peak at which we have moved one
    else:
        right=mid-1
    if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
        Ans=mid
print(Ans)
# it is a good question
