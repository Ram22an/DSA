def Merge(arr,left,mid,right):
    global Counter
    j = mid + 1
    for i in range(left, mid + 1):
        while j <= right and arr[i] > 2 * arr[j]:
            j += 1
        Counter += (j - (mid + 1))
    # this is the part which is changed 
    # here is an example
    # Suppose we have the following two sorted halves from a merge sort:
    # Left half: [5, 7] (indices left = 0 to mid = 1)
    # Right half: [1, 3] (indices mid+1 = 2 to right = 3)
    # Let’s go through the code:

    # Initialization:

    # j is set to mid + 1 = 2.
    # Counter is initially 0.
    # For i = 0: (i.e. arr[0] = 5)

    # Check: Is j (index 2) within the right half? Yes, because j = 2 ≤ right = 3.
    # Check: Does arr[0] > 2 * arr[2]?
    # 5 > 2 * 1 → 5 > 2 is true.
    # So, we increment j. Now, j becomes 3.
    # Now, with j = 3:
    # Check: Is j ≤ right? Yes, 3 ≤ 3. Check: Does arr[0] > 2 * arr[3]?
    # 5 > 2 * 3 → 5 > 6 is false.
    # The while loop stops.
    # Counting for i = 0:
    # The valid indices in the right half for i = 0 are from index mid+1 = 2 to j-1 = 2.
    # That’s j - (mid + 1) = 3 - 2 = 1 pair.
    # We add 1 to Counter (now Counter = 1).
    # For i = 1: (i.e. arr[1] = 7)

    # We do not reset j; it is currently 3.
    # Check: Is j = 3 ≤ right = 3? Yes.
    # Check: Does arr[1] > 2 * arr[3]?
    # 7 > 2 * 3 → 7 > 6 is true.
    # So, increment j. Now, j becomes 4.
    # Now, j = 4 is out of range (since right = 3).
    # The while loop stops.
    # Counting for i = 1:
    # The valid indices in the right half for i = 1 are from index mid+1 = 2 to j-1 = 3.
    # That’s j - (mid + 1) = 4 - 2 = 2 pairs.
    # We add 2 to Counter (now Counter = 1 + 2 = 3).
    tempLeft=left
    tempRight=right
    tempMid=mid+1
    TempArr=[]
    while tempLeft<=mid and tempMid<=right:
        if arr[tempLeft]<=arr[tempMid]:
            TempArr.append(arr[tempLeft])
            tempLeft+=1
        else:
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
nums=list(map(int,input().strip().split()))
Size=len(nums)
Counter=0
Left=0
Right=Size-1
Pairs=[]
MergeSort(nums,Left,Right)
print(Counter,nums,Pairs)
# it was similar to Count Inversion question and approach was 
# also same but some minor changes were done
