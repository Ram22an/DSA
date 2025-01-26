# nums=list(map(int,input().strip().split()))
# Sum=int(input().strip())
# count=0
# Size,i,j,Length=len(nums),0,0,0
# while i<Size:
#     j=i
#     nums_Sum=0
#     while j<Size:
#         nums_Sum+=nums[j]
#         if Sum==nums_Sum:
#             count+=1
#         j+=1
#     i+=1
# print(count)
# this is taking a lot of time 👆🏻

# this is using prefix sum approach 👇🏻
nums=list(map(int,input().strip().split()))
Sum=int(input().strip())
PreFixSum,Count,Size=0,0,len(nums)
HashMap={}
HashMap[0]=1
for i in range(Size):
    PreFixSum+=nums[i]
    if PreFixSum-Sum in HashMap:
        Count+=HashMap[PreFixSum-Sum]
    HashMap[PreFixSum] = HashMap.get(PreFixSum, 0) + 1
    # it retrieves value of PreFixSum if it exists. Otherwise, it defaults to 0.
print(Count)
# this is kind a difficult problem 
