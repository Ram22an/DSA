nums=list(map(int,input().split()))
k=int(input())
# temp=nums[:]
# for i in range(len(nums)):
#     temp[(i+k)%len(nums)]=nums[i]
# for i in range(len(temp)):
#     nums[i]=temp[i]
# this is my original code and this is working
n = len(nums)
k = k % n  # Handle cases where k is greater than the length of nums
temp = nums[:]  # Create a copy of the original list
for i in range(n):
    nums[(i+k)%n] = temp[i]
print(nums)
# this is also working
