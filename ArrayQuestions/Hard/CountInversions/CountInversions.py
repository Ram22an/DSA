# arr=list(map(int,input().strip().split()))
# Size=len(arr)
# Counter=0
# for i in range(Size):
#     for j in range(i+1,Size):
#         if arr[i]>arr[j]:
#             Counter+=1
# print(Counter)
# this is taking a lot of time 👆🏻

def Merge(arr,left,mid,right):
    tempLeft=left
    tempRight=right
    tempMid=mid+1
    TempArr=[]
    while tempLeft<=mid and tempMid<=right:
        if arr[tempLeft]<=arr[tempMid]:
            TempArr.append(arr[tempLeft])
            tempLeft+=1
        else:
            global Counter
            Counter += (mid - tempLeft + 1)
            TempArr.append(arr[tempMid])
            tempMid += 1
    while tempLeft<=mid:
        TempArr.append(arr[tempLeft])
        tempLeft+=1
    while tempMid<=right:
        TempArr.append(arr[tempMid])
        tempMid+=1
    for i in range(len(TempArr)):
        arr[left+i]=TempArr[i]

def MergeSort(arr,left,right):
    if left>=right:
        return
    mid=(left+right)//2
    MergeSort(arr,left,mid)
    MergeSort(arr,mid+1,right)
    Merge(arr,left,mid,right)

# we can you an appraoch merge sort or divide and conquer
arr=list(map(int,input().strip().split()))
Size=len(arr)
Counter=0
Left=0
Right=Size-1
MergeSort(arr,Left,Right)
print(Counter,arr)
# this is kind a difficult problem
