# First approach is very simple i,j,k three loops
# nums=list(map(int,input().strip().split()))
# Size=len(nums)
# Ans=set()
# for i in range(Size):
#     for j in range(i+1,Size):
#         for k in range(j+1,Size):
#             if nums[i]+nums[j]+nums[k]==0 and i!=j and j!=k and i!=k:
#                 Temp=[nums[i],nums[j],nums[k]]
#                 Temp.sort()
#                 Ans.add(tuple(Temp))
# print(Ans)
# this is taking more time than excepted so not good 👆🏻


# for second approach we will use hash map approach using only i and j
# arr[k]=-(arr[i]+arr[j]) if arr[k] in hash map then we found the set
# nums=list(map(int,input().strip().split()))
# Size=len(nums)
# Ans=set()
# for i in range(Size):
#     HashMap={}
#     for j in range(i+1,Size):
#         if -(nums[i]+nums[j]) in HashMap and HashMap[-(nums[i]+nums[j])]!=i and HashMap[-(nums[i]+nums[j])]!=j:
#             temp=[nums[i],nums[j],-(nums[i]+nums[j])]
#             temp.sort()
#             Ans.add(tuple(temp))
#         HashMap[nums[j]]=j
# print(Ans)
# it is still giving time limit exceeded 👆🏻


# For third approach we will use two pointer approach and a sorted array
nums=list(map(int,input().strip().split()))
Size=len(nums)
nums.sort()
Ans=[]
for i in range(Size):
    if i>0 and nums[i]==nums[i-1]:
        continue
    j=i+1
    k=Size-1
    while j<k:
        Sum=nums[i]+nums[j]+nums[k]
        if Sum<0:
            j+=1
        elif Sum>0:
            k-=1
        else:
            temp=[nums[i],nums[j],nums[k]]
            Ans.append(temp)
            j+=1
            k-=1
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1
print(Ans)
# this is a difficult question 
