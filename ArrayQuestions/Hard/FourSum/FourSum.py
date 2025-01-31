# this is similar to three sum all three approaches
nums=list(map(int,input().strip().split()))
Size=len(nums)
nums.sort()
Target=int(input().strip())
Ans=[]
for i in range(Size):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,Size):
        if j!=i+1 and nums[j]==nums[j-1]:
            continue
        k=j+1
        l=Size-1
        while k<l:
            TotalSum=nums[i]+nums[j]+nums[k]+nums[l]
            if TotalSum==Target:
                temp=[nums[i],nums[j],nums[k],nums[l]]
                Ans.append(temp)
                k+=1
                l-=1
                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while k<l and nums[l]==nums[l+1]:
                    l-=1
            elif TotalSum<Target:
                k+=1
            elif TotalSum>Target:
                l-=1
print(Ans)
# this is similar to three sum so i felt easy but it is not
