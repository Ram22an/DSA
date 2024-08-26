arr=list(map(int,input().split()))
mx = arr[0]
for i in range(1, len(arr)):
    if arr[i] > mx:
        mx = arr[i]
print(mx)
