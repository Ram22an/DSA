nums=list(map(int,input().strip().split()))
Size=len(nums)
CompareSize=Size/3
HashMap={}
Ans=set()
for i in nums:
    HashMap[i] = HashMap.get(i, 0) + 1
    if HashMap[i]>CompareSize:
        Ans.append(i)
print(list(Ans))
# it is easy question i have submited this question only in one try and it is accepted
