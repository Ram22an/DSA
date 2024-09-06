arr=list(map(int,input().split()))
MaxElement=arr[0]
for i in range(1,len(arr)):
    if arr[i]>MaxElement:
        MaxElement=arr[i]
SecondMAX=-1
for i in range(0,len(arr)):
    if arr[i]>SecondMAX and arr[i]<MaxElement:
        SecondMAX=arr[i]
print(SecondMAX)
