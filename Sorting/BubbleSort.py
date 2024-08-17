arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
# it is an easy sorting algo and its complexity is O(n^2)
