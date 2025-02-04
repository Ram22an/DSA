# nums1=list(map(int,input().strip().split()))
# nums2=list(map(int,input().strip().split()))
# nums1 = [i for i in nums1 if i != 0]
# nums2 = [i for i in nums2 if i != 0]
# nums3 = nums1[:] + nums2[:]
# nums3.sort()
# nums1[:]=nums3[:]
# this was my approach i don't know why it is not working 👆🏻

# but this worked
nums1=list(map(int,input().strip().split()))
nums2=list(map(int,input().strip().split()))
m=len(nums1)
n=len(nums2)
for i in range(n):
        nums1[m+i]=nums2[i]
nums1.sort()
# this will not work here as nums1 should have size of m+n from starting
