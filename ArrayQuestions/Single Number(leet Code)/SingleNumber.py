nums=list(map(int,input().strip().split()))
temp={}
for i in nums:
    if i not in temp:
        temp[i]=1
    else:
        temp[i]+=1
for i in nums:
    if temp[i]==1:
        print(i)
        break
# this was an easy one
