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

        