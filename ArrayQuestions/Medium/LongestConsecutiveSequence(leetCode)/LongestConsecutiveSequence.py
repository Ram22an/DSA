# nums=list(map(int,input().strip().split()))
# nums.sort()
# print(nums)
# nums=set(nums)
# nums=list(nums)
# nums.sort()
# print(nums)
# Size=len(nums)
# i=0
# LongestSizeEndIndex=0
# LongestSizeStartIndex=0
# LongestSize=0
# while i<Size-1:
#     if -1<nums[i+1]-nums[i]<=1:
#         LongestSizeStartIndex=i
#         while i<Size-1 and 0<=nums[i+1]-nums[i]<=1 :
#             i+=1
#         LongestSizeEndIndex=i
#         LongestSize=LongestSizeEndIndex-LongestSizeStartIndex
#     else:
#         i+=1
# print(LongestSize+1)
# this is a good code but not passing all the test cases 👆🏻
import sys
nums=list(map(int,input().strip().split()))
num_set = set(nums)
longest = 0
for num in num_set:
    if num - 1 not in num_set:  # Start of a sequence
        current_num = num
        count = 1
        while current_num + 1 in num_set:
            current_num += 1
            count += 1
        longest = max(longest, count)
print(longest)
# this is working code
