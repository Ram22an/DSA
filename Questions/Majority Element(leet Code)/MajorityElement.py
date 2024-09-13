def FindMajorityElement(nums):
    Dict={}
    for i in range(len(nums)):
        if nums[i] not in Dict:
            Dict[nums[i]]=1
        else:
            Dict[nums[i]]+=1
    for i in Dict:
        if Dict[i]>=len(nums)/2:
            return i
nums=list(map(int,input().strip().split()))
ans=FindMajorityElement(nums)
print(ans)
# this was a easy question 
