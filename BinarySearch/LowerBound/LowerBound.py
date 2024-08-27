Arr=list(map(int,input().split()))
Arr.sort()
# lower bound is smallest index such that Arr[ind]>=x
# we will apply binary search
x=int(input())
ans=len(Arr)
right=len(Arr)-1
left=0
while left<=right:
    mid=(left+right)//2
    if Arr[mid]>=x:
        ans=mid
        right=mid-1
    else:
        left=mid+1
print(ans)
# we can find it in linear fashion but it will take 
# n time but it is taking logn time
