def Sorting(arr,left,mid,right):
    starting=left
    ending=right
    center=mid+1
    temp=[]
    while starting<=mid and center<=right:
        if arr[starting]<arr[center]:
            temp.append(arr[starting])
            starting+=1
        else:
            temp.append(arr[center])
            center+=1
    while starting<=mid:
        temp.append(arr[starting])
        starting+=1
    while center<=right:
        temp.append(arr[center])
        center+=1
    for i in range(len(temp)):
        arr[left+i]=temp[i]
def MergeSort(arr,left,right):
    mid=(left+right)//2
    if left>=right:
        return
    MergeSort(arr,left,mid)
    MergeSort(arr,mid+1,right)
    Sorting(arr,left,mid,right)
arr=list(map(int,input().split()))
MergeSort(arr,0,len(arr)-1)
print(arr)
# here is the merge sort aglo and its time complexity is O(nlogn) and space complexity is O(n)
# it is better than bubble,insertion and selection in term of time complexity 
