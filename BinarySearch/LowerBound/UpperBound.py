# upper bound is nothing but arr[ind]>target
Arr=list(map(int,input().split()))
Arr.sort()
x=int(input())
ans=len(Arr)
right=len(Arr)-1
left=0
while left<=right:
    mid=(left+right)//2
    if Arr[mid]>x:
        ans=mid
        right=mid-1
    else:
        left=mid+1
print(ans)