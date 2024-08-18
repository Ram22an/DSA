def Sorting(Arr,low,high):
    pivot = Arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and Arr[i] <= pivot:
            i += 1
        while i <= j and Arr[j] >= pivot:
            j -= 1
        if i <= j:
            Arr[i], Arr[j] = Arr[j], Arr[i]
        else:
            break

    Arr[low], Arr[j] = Arr[j], Arr[low]
    return j   
def QuickSort(Arr,low,high):
    if low<high:
        partion=Sorting(Arr,low,high)
        QuickSort(Arr,low,partion-1)
        QuickSort(Arr,partion+1,high)
    return
Arr=list(map(int,input().split()))
QuickSort(Arr,0,len(Arr)-1)
print(Arr)
# this is kind a tough algo to implement but it is easy to remember like what we have to do
# its code implement is difficult we have to put smaller at the left hand side and larger at right hand side
