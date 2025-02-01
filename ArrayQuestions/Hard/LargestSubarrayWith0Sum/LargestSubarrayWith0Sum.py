# this is taking too much time
# arr=list(map(int,input().strip().split()))
# Size=len(arr)
# i,length=0,0
# while i<Size:
#     Sum=arr[i]
#     j=i+1
#     while j<Size:
#         Sum+=arr[j]
#         if Sum==0:
#             length=max(length,j-i+1)
#         j+=1
#     i+=1
# print(length)

# in this question we will use kadan's algorithm
# or subarray sum equal to k 
arr=list(map(int,input().strip().split()))
Size=len(arr)
Sum=0
PreFixSum,Length=0,0
HashMap={}
for i in range(Size):
    PreFixSum+=arr[i]
    if PreFixSum==0:
        Length=i+1
    else:
        if HashMap.get(PreFixSum)is not None:
            Length=max(Length,i-HashMap[PreFixSum])
        else:
            HashMap[PreFixSum]=i
print(Length)