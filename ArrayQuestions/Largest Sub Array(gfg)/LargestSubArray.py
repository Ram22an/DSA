def lenOfLongSubarr(arr, n, k):
        prefix_sum = {}
        cumulative_sum = 0
        max_size = 0
        for i in range(n):
            cumulative_sum += arr[i]
            # If cumulative_sum equals k, we found a subarray from index 0 to i
            # why we are not checking cumulative_sum>=k cumulative_sum could be greater than k when added
            # we are checking here for first few iteration like for starting ones
            if cumulative_sum == k:
                # example when max_size=0 then we find sub array start from 0 and goes to 3 so len will be 4
                max_size = i + 1
            # If (cumulative_sum - k) exists in the dictionary, we found a subarray
            if cumulative_sum - k in prefix_sum:
                # it cumulative_sum=6 and k=3 so there exist an array with sum of 3
                # The subarray sum equals k between prefix_sum[cumulative_sum - k] and i
                max_size = max(max_size, i - prefix_sum[cumulative_sum - k])
            # Store cumulative_sum in the dictionary if not already present
            if cumulative_sum not in prefix_sum:
                # here simply we are adding the cumulative_sum to hash map
                prefix_sum[cumulative_sum] = i
        return max_size
arr=list(map(int,input().strip().split()))
k=int(input())
lenOfLongSubarr(arr,len(arr),k)
# this logic was difficult for me to understand
