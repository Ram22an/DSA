Arr=list(map(int,input().split()))
Arr.sort()
# temp=[]
# for i in range(len(nums)):
#     if nums[i] not in temp:
#         temp.append(nums[i])
# for j in range(len(temp)):
#     nums[j] = temp[j]
# return len(temp)
# this is my code it is working fine and is also accepted
# here is more complex code which might look good 
if not Arr:
    print(0)
# Initialize a pointer for the position of the unique elements
k = 1
for i in range(1, len(Arr)):
    if Arr[i] != Arr[i - 1]:
    # If the current number is different from the previous one, it's unique
        Arr[k] = Arr[i]
        k += 1        
print(k)
# this code is also accepted
