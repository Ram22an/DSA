nums=list(map(int,input().split()))
count_breaks = 0
TrueorFalse=True
n = len(nums)    
for i in range(n):
    if nums[i] > nums[(i + 1) % n]:
        count_breaks += 1
    if count_breaks > 1:
        TrueorFalse=False
        break
print(TrueorFalse)
# here we are checking if the break or inconsistency is there or not
# we are only expceting there is only one i.e. smallest and the largest difference
# we are checking for the last and first specially and if there are any other than
# we have to break it
