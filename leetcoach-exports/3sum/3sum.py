class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                return res
            elif i != 0 and nums[i] == nums[i - 1]:
                i += 1
            else:
                target = -1 * nums[i]
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    summed = nums[l] + nums[r]
                    if summed == target:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif summed > target:
                        r -= 1
                    else:
                        l += 1
                i += 1
        return res