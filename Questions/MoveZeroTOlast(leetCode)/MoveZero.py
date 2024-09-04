nums=list(map(int,input().split()))
temp=[]
for i in range(len(nums)):
    if nums[i]!=0:
        temp.append(nums[i])
diff=len(nums)-len(temp)
for i in range(diff):
    temp.append(0)
for i in range(len(nums)):
    nums[i]=temp[i]
print(nums)
# it is an easy question
