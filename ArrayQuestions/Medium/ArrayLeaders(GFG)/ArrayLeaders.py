# arr=list(map(int,input().strip().split()))
# leaders=[]
# Size=len(arr)
# for i in range(Size):
#     Temp=arr[i:]
#     if max(Temp)<=arr[i]:
#         leaders.append(arr[i])
# print(leaders)
# this code is taking more time 👆🏻

arr=list(map(int,input().strip().split()))
maxElement=arr[-1]
leaders=[]
leaders.append(arr[-1])
Size=len(arr)-2
for i in range(Size,-1,-1):
    if arr[i]>=maxElement:
        maxElement=arr[i]
        leaders.append(arr[i])
leaders[:]=leaders[::-1]
print(leaders)
# this question was easy but the my approach is taking more time
# but this approach it taking on bigO of n 
# here we are starting from end and then making the largest element as last
# and then comparing it to the next element if it is bigger if yes
# then add it to the leaders
