nums=list(map(int,input().strip().split()))
PositiveArray=[]
NegativeArray=[]
Size=len(nums)
for i in range(Size):
    if nums[i]<0:
        NegativeArray.append(nums[i])
    else:
        PositiveArray.append(nums[i])
finalArray=[]
for i in range(Size//2):
    finalArray.append(PositiveArray[i])
    finalArray.append(NegativeArray[i])
print(finalArray)
# it was easy question
