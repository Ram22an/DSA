# to submit this question i have to subscribe leetcode premium

# So question is like i have given array of coordinate of gas station and they will be in sorted order
# and you also given number of new gas station to be added that is k

nums=list(map(int,input().strip().split()))
k=int(input())

# this is the naive approach
# Size=len(nums)
# HowMany=[0]*(Size-1)
# for _ in range(1,k+1):
#     MAxVal=-1
#     MaxIndex=-1
#     for i in range(Size-1):
#         Diff=nums[i+1]-nums[i]
#         SectionLength=Diff/(HowMany[i]+1)
#         if MAxVal<SectionLength:
#             MAxVal=SectionLength
#             MaxIndex=i
#     if MaxIndex != -1:
#         HowMany[MaxIndex] += 1
# MaxAns=-1
# for i in range(Size-1):
#     SectionLength=(nums[i+1]-nums[i])/(HowMany[i]+1)
#     MaxAns=max(MaxAns,SectionLength)
# print(MaxAns)
# this could the wrong or it will go time limite exceeded

# in new approach we will use PRIORITY queue
# import heapq
# pq=[]
# Size=len(nums)
# for i in range(Size - 1):
#     heapq.heappush(pq, (-(nums[i+1] - nums[i]), i))
# Sector=[0]*(Size-1)
# for _ in range(k):
#     Current, Index = heapq.heappop(pq)
#     Sector[Index] += 1
#     InDeff=nums[Index+1]-nums[Index]
#     NewSecLen=InDeff/(Sector[Index]+1)
#     heapq.heappush(pq,(NewSecLen*(-1),Index))
# top_element = -pq[0][0]
# print(top_element)

# in optimal solution we will use binary search
# there is difference in binary search which we will apply in this question please refer the image
def CountGasStation(arr,mid,Size):
    Cout=0
    # for i in range(1,Size-1):
    #     NumberBetween=(arr[i+1]-arr[i])/mid
    #     if (arr[i+1]-arr[i])/mid==NumberBetween*mid:
    #         NumberBetween-=1
    #     Cout+=NumberBetween
    # return Cout
    for i in range(Size - 1):  # Loop should start from `0`
        NumberBetween = (arr[i+1] - arr[i]) // mid  # Integer division
        Cout += NumberBetween
    return Cout
MaxDiff=-1
Size=len(nums)
for i in range(Size-1):
    MaxDiff=max(MaxDiff,nums[i+1]-nums[i])
low=0
high=MaxDiff
Limit=pow(10,-6)
while high-low>Limit:
    mid=(high+low)/2.0
    Count=CountGasStation(nums,mid,Size)
    if Count>k:
        low=mid
    else:
        high=mid
print(high)
# this is some what working i don't know the exact working
# yeh question bahut difficult hai
