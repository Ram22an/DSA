def BinarySearch(arr,left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return BinarySearch(arr,left,mid-1,target)
    else:
        return BinarySearch(arr,mid+1,right,target)
# in this searching the array should be sorted
Arr=list(map(int,input().split()))
Arr.sort()
Target=int(input("Enter the number to be found "))
Left=0
Right=len(Arr)-1
print(BinarySearch(Arr,Left,Right,Target))
