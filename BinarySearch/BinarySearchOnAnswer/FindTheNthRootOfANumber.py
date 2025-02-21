n,m=map(int,input().strip().split())
Ans=-1
left=1
right=m
while left<=right:
    mid=(left+right)//2
    if pow(mid,n)==m:
        print(mid)
        break
    if pow(mid,n)>m:
        right=mid-1
    else:
        left=mid+1
print(-1)
# it is a good question
