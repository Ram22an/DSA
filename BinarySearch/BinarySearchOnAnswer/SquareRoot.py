n=int(input())
Ans=1
left=1
right=n
while left<=right:
    mid=(left+right)//2
    # i forgot the case
    if mid * mid == n:  # Perfect square case
        print(mid)
        break
    if mid*mid<n:
        left=mid+1
        Ans=mid
    if mid*mid>n:
        right=mid-1
print(Ans)
# this is kind a interseting question
