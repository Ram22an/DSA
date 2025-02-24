arr=list(map(int,input().strip().split()))
k=int(input())

# this is my first appraoch
# Starting=1
# counter=0
# missing=[]
# while True:
#     if Starting not in arr:
#         missing.append(Starting)
#         counter+=1
#     if counter==k:
#         print(missing[k-1])
#         break
#     Starting+=1
# this is passing all the cases but taking a lot of time

# here is the second appraoch
# for i in arr:
#     if i<=k:
#         k+=1
#     else:
#         print(k)
#         break
# print(k)
# this is The approach is greedy and incremental
# this work like 1 2 3 4 5 6 7 8 9 10 11
# and the array is 2 3 4 7 11
# and k is 5
# so in question it is given that there are no negative and 0 in array so it start with 1
# so when we encounter 2 so we shift 5 as 2 is smaller than 5 and it become 6
# and for 3 also it become 7 and for 4 it become 8 and for 7 it become 9
# for 11 as 9 is smaller then 11 so our answer is 9

# we can apply binary search here but it is not tipical binary search
left=0
Size=len(arr)
right=Size-1
while left<=right:
    mid=(left+right)//2
    missing=arr[mid]-(mid+1)
    if missing<k:
        left=mid+1
    else:
        right=mid-1
print(right+1+k,left+k)
# this is the implementation of binary search
