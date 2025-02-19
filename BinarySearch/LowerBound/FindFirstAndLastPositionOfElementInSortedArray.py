# here we will use upper bound arr[ind]>x and lower bound arr[ind]>=x
# nums=list(map(int,input().strip().split()))
# target=int(input())
# also check for empty array
# if not nums:
#     print(-1, -1)
# if len(nums)==1 and nums[0]==target:
#     print(0,0)
# ansUpperBound=-1
# right=len(nums)-1
# left=0
# while left<=right:
#     mid=(left+right)//2
#     if nums[mid]>target:
#         right=mid-1
#     else:
#         left=mid+1
# ansUpperBound=left-1
# ansLowerBound=-1
# right=len(nums)-1
# left=0
# while left<=right:
#     mid=(left+right)//2
#     if nums[mid]>=target:
#         ansLowerBound=mid
#         right=mid-1
#     else:
#         left=mid+1
# if ansLowerBound==len(nums) or nums[ansLowerBound]!=target:
#     print(-1,-1)
# else:
#     print(ansLowerBound,ansUpperBound)
# it is very tough question it is not done by me i will try it tomorrow or later


# this i tried to understand the question and implemented the logic
nums=list(map(int,input().strip().split()))
target=int(input())
if not nums:
    print(-1, -1)
if len(nums)==1 and nums[0]==target:
    print(0,0)
StartingPosition=-1
EndingPosition=-1
# here we will find upper bound that is arr[ind]>x
left=0
right=len(nums)-1
mid=0
while left<=right:
    mid=(left+right)//2
    if nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
EndingPosition=mid-1

# here we will find lower bound that is arr[ind]>=x
left=0
right=len(nums)-1
mid=0
while left<=right:
    mid=(left+right)//2
    if nums[mid]>=target:
        right=mid-1
    else:
        left=mid+1
if StartingPosition==len(nums) or nums[StartingPosition]!=target:
    print(-1,-1)
else:
    print(StartingPosition,EndingPosition)
