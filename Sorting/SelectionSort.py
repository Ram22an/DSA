# select the minimum from the array
Arr=list(map(int,input().split()))
for i in range(len(Arr)):
    for j in range(i,len(Arr)):
        if Arr[i]>Arr[j]:
            temp=Arr[i]
            Arr[i]=Arr[j]
            Arr[j]=temp
print(Arr)
# it is one of the most simplest sorting array
# its time complexity is n^2 
