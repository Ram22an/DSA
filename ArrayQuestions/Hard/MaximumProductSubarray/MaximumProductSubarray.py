import sys
nums=list(map(int,input().strip().split()))
Size=len(nums)
PrefixProduct,SubFixProduct=1,1
MaxProduct=-sys.maxsize
for i in range(Size):
    if PrefixProduct==0:
        PrefixProduct=1
    if SubFixProduct==0:
        SubFixProduct=1
    PrefixProduct*=nums[i]
    SubFixProduct*=nums[Size-1-i]
    MaxProduct=max(SubFixProduct,PrefixProduct,MaxProduct)
print(MaxProduct)
# this was kind a easy question but you alway go with observation
# and for sub array alway go with subfix or prefix approach
