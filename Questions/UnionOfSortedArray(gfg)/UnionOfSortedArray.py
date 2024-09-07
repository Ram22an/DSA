
if __name__=="__main__":
    n,m=map(int,input().strip().split())
    arr1=list(map(int,input().strip().split()))
    arr2=list(map(int,input().strip().split()))
    i = 0
    j = 0
    temp1 = []
    # this code is also working
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not temp1 or temp1[-1] != arr1[i]:  # Check to avoid duplicates
                temp1.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if not temp1 or temp1[-1] != arr2[j]:  # Check to avoid duplicates
                temp1.append(arr2[j])
            j += 1
        else:  # arr1[i] == arr2[j]
            if not temp1 or temp1[-1] != arr1[i]:  # Check to avoid duplicates
                temp1.append(arr1[i])
            i += 1
            j += 1

    # Append remaining elements from arr1
    while i < n:
        if not temp1 or temp1[-1] != arr1[i]:  # Check to avoid duplicates
            temp1.append(arr1[i])
        i += 1

    # Append remaining elements from arr2
    while j < m:
        if not temp1 or temp1[-1] != arr2[j]:  # Check to avoid duplicates
            temp1.append(arr2[j])
        j += 1
    # temp1=[]
    # for i in range(len(arr1)):
    #     if arr1[i] not in temp1:
    #         temp1.append(arr1[i])
    # for i in range(len(arr2)):
    #     if arr2[i] not in temp1:
    #         temp1.append(arr2[i])
    # temp1.sort()
    # return temp1
    # temp1 = []
    # temp2=arr1+arr2
    # for i in temp2:  # Combine arr1 and arr2 into a single loop
    #     if i not in temp1:
    #         temp1.append(i)
    # temp1.sort()
    # return temp1 
    # i=0
    # j=0
    # temp1=[]
    # while i<n and j<m:
    #     if arr1[i] < arr2[j]:
    #         temp1.append(arr1[i])
    #         i += 1
    #     elif arr2[j] < arr1[i]:
    #         temp1.append(arr2[j])
    #         j += 1
    #     else:
    #         temp1.append(arr1[i])
    #         i += 1
    #         j += 1
    # while i<n:
    #     temp1.append(arr1[i])
    #     i+=1
    # while j<m:
    #     temp1.append(arr2[j])
    #     j+=1
    # temp2=[]
    # for i in temp1:
    #     if i not in temp2:
    #         temp2.append(i)
    # return temp2
    # return sorted(set(arr1).union(arr2))
    # i have tried a lot but this is only working code
