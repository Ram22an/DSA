def findMissingAndRepeating(arr):
    n = len(arr)
    
    # Expected sum and sum of squares
    Sn = n * (n + 1) // 2
    Ssqn = n * (n + 1) * (2 * n + 1) // 6
    
    # Actual sum and sum of squares in array
    S1 = sum(arr)
    S2 = sum(x * x for x in arr)
    
    # Equations to solve
    diff = S1 - Sn        # (b - a)
    sum_diff = S2 - Ssqn  # (b^2 - a^2)
    
    # Solve for a and b using (b^2 - a^2) = (b - a)(b + a)
    sum_ab = sum_diff // diff  # (b + a)
    
    # Finding a and b
    b = (diff + sum_ab) // 2
    a = b - diff
    
    return [b, a]
arr = list(map(int, input().split()))
print(findMissingAndRepeating(arr))
# This code efficiently finds the missing and repeating numbers in 
# an unsorted array of size n. The key idea is to use mathematical properties 
# instead of extra space. First, we calculate the expected sum (Sn) and 
# sum of squares (Ssqn) for numbers from 1 to n using the formulas Sn = n(n+1)/2 
# and Ssqn = n(n+1)(2n+1)/6. Next, we compute the actual sum (S1) and 
# sum of squares (S2) from the given array. By taking the difference diff = S1 - Sn, 
# we get (b - a), where b is the repeating number and a is the missing number. Similarly, 
# using sum_diff = S2 - Ssqn, we derive (b² - a²). Since (b² - a²) = (b - a)(b + a), 
# we solve for (b + a). By adding and solving the two equations, we find the values of b and a.
# For example, given the array [4, 3, 6, 2, 1, 1], we determine that 1 is the 
# repeating number and 5 is the missing number. This approach runs in O(n) time complexity 
# and uses only constant space.
