def CanMove(arr,mid,dayToBeDone):
    Days=1
    load=0
    for i in arr:
        if load+i>mid:
            Days+=1
            load=i
        else:
            load+=i
        if Days>dayToBeDone:
            return False
    return True
    
weights=list(map(int,input().strip().split()))
days=int(input())
Ans=max(weights)
left=Ans
right=sum(weights)
while left<=right:
    mid=(left+right)//2
    # it must load packages sequentially!
    # so this approach is not correct 👇🏻
    # temp=TotalSum
    # Counter=1
    # while temp>=0:
    #     temp=temp-mid
    #     Counter+=1

    # this is working but i need code with good time complexity
    # if CanMove(weights,mid,days):
    #     Ans=mid
    #     right=mid-1
    # else:
    #     left=mid+1
    dayToBeDone=1
    load=0
    for i in weights:
        if load+i>mid:
            dayToBeDone+=1
            load=i
            if dayToBeDone>days:
                break
        else:
            load+=i
    if dayToBeDone>days:
        left=mid+1
    else:
        Ans=mid
        right=mid-1
print(Ans)
