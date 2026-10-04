class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = []
        loc = {}
        for i, num in enumerate(nums):
            if i != 0:
                prefix.append((prefix[i - 1] + num))
            else:
                prefix.append(num)
            rem = prefix[i] % k
            if (rem == 0 and len(prefix) >= 2 and (prefix[i] >= k or prefix[i] == 0)) or (rem in loc and ((i - loc[rem]) >= 2)):
                return True
            if rem not in loc:
                loc[rem] = i
        return False
        
# [15, 12, 12, 12, 16] k = 36
    # [15, 27, 39, 51]
    # Ohhh so if at any point you see the same reccurence of mod
    # then you know from i + 1 until the current val must be the right 
    # coimbinaiton of nums
    # cuz if you exlcude everyhting before it then you have an answer
    # thgats crazyyyy 

# Given an integer array nums and an int k, return true if nums has a good subarray
# Subarray is a contigous part of the array
# an integer x is a multiple of k if there exists an integer s.t. x = n * k
    # 0 is alwas a multiple of k

# Two pointer works until there is negatives

# Try and focus on remainders? 
    # Prefix sum, then remainder 
    # Why prefix sum? we're doing subarrays
    # the problem with prefix sum is that it is a running sum
        # So we can't exclude elements beforehand
        # but there's something else thats interesting
            # You get a running total
            # then hash the remainder
            # 