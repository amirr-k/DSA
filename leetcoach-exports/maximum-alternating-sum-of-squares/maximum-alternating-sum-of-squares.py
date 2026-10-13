class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x))
        res = 0 
        l, r = 0, len(nums) - 1
        while l < r:
            res += (nums[r] ** 2)
            res -= (nums[l] **2)
            l += 1
            r -= 1
        if l == r:
            res += (nums[r] **2)
        else:
            return res
        return res

        
# Given integer array nums

# Return an integer denoting the max possible alternating score of nums after rearranging
