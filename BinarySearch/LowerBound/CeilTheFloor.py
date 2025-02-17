def getFloorAndCeil( x, arr: list) -> list:
    arr.sort()
    ansFloor=-1
    ansCeiling=-1
    right=len(arr)-1
    left=0
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            return [arr[mid], arr[mid]]
        elif arr[mid]>x:
            ansCeiling=mid
            right=mid-1
        else:
            ansFloor=mid
            left=mid+1
    floorVal = arr[ansFloor] if ansFloor != -1 else -1
    ceilVal = arr[ansCeiling] if ansCeiling != -1 else -1
    return [floorVal, ceilVal]
arr=list(map(int,input().strip().split()))
x=int(input())
print(getFloorAndCeil(x,arr))
# in this question we have to find the element which is smaller and greater than x
# so tips are read question properly and you don't have to return index but element
