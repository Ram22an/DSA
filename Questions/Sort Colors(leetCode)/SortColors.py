def SortRWBInPlace(nums):
    Dict={0:0,1:0,2:0}
    for i in range(len(nums)):
        Dict[nums[i]]+=1
    temp0=[0]*Dict[0]
    temp1=[1]*Dict[1]
    temp2=[2]*Dict[2]
    temp3=temp0+temp1+temp2
    nums[:]=temp3
nums=list(map(int,input().strip().split()))
SortRWBInPlace(nums)
print(nums)
# it was easy question and i could have done the question in first try 
# but i didn't know how to modify array inplace but now i know
