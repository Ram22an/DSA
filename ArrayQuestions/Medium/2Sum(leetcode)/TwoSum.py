nums=list(map(int,input().strip().split()))
target=int(input())
Dict={}
for i in range(len(nums)):
    if target-nums[i] in Dict:
        print([Dict[target-nums[i]],i])
        break
    Dict[nums[i]]=i
# it was not easy but also kinda easy 
# Note:- if you learned something don't just 
# simply go with the same thing every time think something different also
