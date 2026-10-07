class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res = 0
        l, r = 0, 0
        runningSum = 0
        leadingZeros = 0
        while r < len(nums):
            runningSum += nums[r]
            if l == r:
                if runningSum == goal:
                    res += 1
            else:
                if runningSum > goal:
                    leadingZeros = 0
                while l <= r and runningSum > goal:
                    runningSum -= nums[l]
                    l += 1

                if l <= r and runningSum == goal:
                    while l < r and nums[l] == 0:
                        leadingZeros += 1
                        l += 1

                    res += 1 + leadingZeros
            r += 1
                

        return res