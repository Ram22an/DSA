nums=list(map(int,input().strip().split()))
target=int(input())
# this is also working
# Found=-1
# Size=len(nums)
# for i in range(Size):
#     if nums[i]==target:
#         Found=i
# print(Found)
try:
    print(nums.index(target))
except ValueError:
    print(-1)
# the question was different i was not able to understand why 
# unnecessary explanation 
