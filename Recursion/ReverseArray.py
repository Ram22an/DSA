def ReverseArr(Arr,i,size):
    if i>=size-1-i:
        return
    temp=Arr[i]
    Arr[i]=Arr[size-1-i]
    Arr[size-1-i]=temp
    return ReverseArr(Arr,i+1,size)
Arr=list(map(int,input().split()))
print(Arr)
ReverseArr(Arr,0,len(Arr))
print(Arr)
