nums=list(map(int,input().strip().split()))
MaxLength=0
CurrentLength=0
for i in range(len(nums)):
    if nums[i]==1:
        CurrentLength+=1
    else:
        CurrentLength=0
MaxLength=max(MaxLength,CurrentLength)
print(MaxLength)
# this was an easy one ;) "1"
