# nums=list(map(int,input().strip().split()))
# Number=0
# nums_set = set(nums)
# for i in nums:
#     Number=Number*10+i
# while True:
#     Number+=1
#     Templist=list(map(int,str(Number)))
#     TemplistSet=set(Templist)
#     if nums_set.issuperset(Templist) and TemplistSet.issuperset(nums):
#         break
# Templist=list(map(int,str(Number)))
# nums=Templist[:]
# print(nums)
# this is not a good approach 👆🏻

# this is kind a close
# nums=list(map(int,input().strip().split()))
# Size=len(nums)-1
# PreFixIndex=Size+1
# for i in range(Size):
#     if nums[i]<nums[i+1]:
#         PreFixIndex=i
# print(PreFixIndex)
# if PreFixIndex!=Size+1:
#     PreFixList=nums[:PreFixIndex]
#     print(PreFixList)
#     PostFixList=nums[PreFixIndex:]
#     # PostFixList.sort()
#     if len(PostFixList)>1:
#         temp=PostFixList[0]
#         PostFixList[0]=PostFixList[1]
#         PostFixList[1]=temp
#     nums[:]=PreFixList[:]+PostFixList[:]
#     print(nums)
# else:
#     nums.sort()
#     print(nums)
import sys
nums=list(map(int,input().strip().split()))
Size=len(nums)-1
preFixIndex=Size+1
for i in range(Size):
    if nums[i]<nums[i+1]:
        preFixIndex=i
if preFixIndex!=Size+1:
    PreFixList=nums[:preFixIndex+1]
    PostFixList=nums[preFixIndex+1:]
    PreFixListMinValue=PreFixList[-1]
    MinDifference=sys.maxsize
    for i in PostFixList:
        if i-PreFixListMinValue>0:
            MinDifference=min(MinDifference,i-PreFixListMinValue)
    FinalMinValuePostFixIndex=0
    for i in PostFixList:
        if i-PreFixListMinValue==MinDifference:
            FinalMinValuePostFixIndex=PostFixList.index(i)
    tempValue=PreFixList[-1]
    PreFixList[-1]=PostFixList[FinalMinValuePostFixIndex]
    PostFixList[FinalMinValuePostFixIndex]=tempValue
    PostFixList.sort()
    nums[:]=PreFixList[:]+PostFixList[:]
    print(nums)

else:
    nums.sort()
    print(nums)
# this is a good question 
# first we have to find the breaking point where nums[i]<nums[i+1]
# and then we have to find the number just greater the nums[i]
# and then swap it with nums[i] and the sort the list after
# nums[i] remember first swap the nums[i] and the number just greater
