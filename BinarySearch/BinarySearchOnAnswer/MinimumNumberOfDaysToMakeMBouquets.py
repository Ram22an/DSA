def NumberOfFlower(arr,Value,Bouquets,FlowersVal):
    Counter=0
    Ans=0
    Size=len(arr)
    for i in range(Size):
        if arr[i]<=Value:
            Counter+=1
            if Counter == FlowersVal:  # Bouquet is completed
                Ans += 1
                Counter = 0
                if Ans>=bouquets:
                    return True
        else:
            Counter=0
    return Ans >= Bouquets 
bloomDay=list(map(int,input().strip().split()))
bouquets=int(input())
Flowers=int(input())
Size=len(bloomDay)
if Size<bouquets*Flowers:
    print(-1)
left=min(bloomDay)
right=max(bloomDay)
Ans=right
while left<=right:
    mid=(left+right)//2
    Temp=NumberOfFlower(bloomDay,mid,bouquets,Flowers)
    if Temp:
        Ans=mid
        right=mid-1
    else:
        left=mid+1
print(Ans)

# today i got to know that using Size=len(nums) is slower then for i in nums
