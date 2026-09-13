class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = None
        i = 0
        while i < len(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                potRes = nums[l] + nums[r] + nums[i]
                if (res is None) or (abs(target - potRes) < abs(target - res)):
                    res = potRes
                if potRes > target:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res
        
# Given integer array
    # find three integers at distinct indices in nums such that sum is closest to target
    # return sum of the three integers
