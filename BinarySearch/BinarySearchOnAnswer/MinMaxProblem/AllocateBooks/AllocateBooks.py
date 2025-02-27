import sys
arr=list(map(int,input().strip().split()))
m=int(input())
n=len(arr)
if n<m:
    print(-1)
    sys.exit()
MAxValue=-sys.maxsize
TotalSum=0
for i in arr:
    if i>=MAxValue:
        MAxValue=i
    TotalSum+=i
left=MAxValue
right=TotalSum

def AllocationOfBook(Arr,MaxPages):
    Student=1
    CurrentPages=0
    for i in Arr:
        if CurrentPages+i<=MaxPages:
            CurrentPages+=i
        else:
            Student+=1
            CurrentPages=i
            if Student > m:
                return Student
    return Student

# here is the implementation with linear search
# for i in range(left,right+1):
#     Ans=AllocationOfBook(arr,i)
#     if Ans==m:
#         print(i)
#         break
while left<=right:
    mid=(left+right)//2
    Temp=AllocationOfBook(arr,mid)
    if Temp>m:
        left=mid+1
    else:
        right=mid-1
print(left)
