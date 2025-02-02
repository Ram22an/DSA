# XOR operation
# A   B   C
# 1	  1	  0
# 0	  1	  1
# 1	  0	  1
# 0	  0	  0
# in python ^ is xor operator
# arr=list(map(int,input().strip().split()))
# Compare=int(input())
# Counter=0
# Size=len(arr)
# for i in range(Size):
#     Sum=0
#     for j in range(i,Size):
#         Sum^=arr[j]
#         if Sum==Compare:
#             Counter+=1
# print(Counter)
# this is causing time limite exceed 👆🏻

arr=list(map(int,input().strip().split()))
Compare=int(input())
HashMap={}
Counter,Size,PreXOR=0,len(arr),0
HashMap[0]=1
for i in range(Size):
    PreXOR^=arr[i]
    if PreXOR^Compare in HashMap:
        Counter+=HashMap[PreXOR^Compare]
    HashMap[PreXOR]=HashMap.get(PreXOR,0)+1
print(Counter)
# i didn't got the concept fully but it is similar to prefix sum type question
