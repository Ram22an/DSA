# this approach is very labrous we can do it in better way
# def Merge(arr,left,mid,right):
#     start=left
#     center=mid+1
#     temp=[]
#     while start<=mid and center<=right:
#         if arr[start]<arr[center]:
#             temp.append(arr[start])
#             start+=1
#         elif arr[center]<arr[start]:
#             temp.append(arr[center])
#             center+=1
#         else:
#             temp.append(arr[start])
#             start+=1
#             center+=1
#     while start<=mid:
#         temp.append(arr[start])
#         start+=1
#     while center<=right:
#         temp.append(arr[center])
#         center+=1
#     for i in range(len(temp)):
#         arr[left+i]=temp[i]
# def MergerSort(Arr,left,right):
#     mid=(left+right)//2
#     if right<=left:
#         return
#     MergerSort(Arr,left,mid)
#     MergerSort(Arr,mid+1,right)
#     Merge(Arr,left,mid,right)
# def FindMissingNumber(Arry,Size):
#     MergerSort(Arry,0,Size-1)
#     print(Arry)
#     for i in range(1,len(Arry)):
#         if Arry[i]-Arry[i-1]>1:
#             return (Arry[i-1]+Arry[i])//2
#     if Arry[-1]!=len(Arry):
#         return len(Arry)
#     if Arry[0]!=0:
#         return 0
#     return -1
Arr=list(map(int,input().strip().split()))
Size=len(Arr)
# ans=FindMissingNumber(Arr,Size)
# print(ans)
# temp=[-1]*(Size+1)
# for i in range(len(Arr)):
#     temp[Arr[i]]=0
# for i in range(len(temp)):
#     if temp[i]==-1:
#         print(i)
# we can do it with xor operation also
# n = len(Arr)
# ans = 0
# for i in range(1, n + 1):
#     ans ^= i
# for num in Arr:
#     ans ^= num
# print(ans)
# i find one more easy solution that is sum of n natural number - sum of numbers in the array
Sum=Size*(Size+1)//2
total=0
for i in Arr:
    total+=i
print(Sum-total)
# this is the best so far
