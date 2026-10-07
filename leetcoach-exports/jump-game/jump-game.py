class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        goal = len(nums) - 1
        i = goal - 1
        while i >= 0:
            if i == 0 and (i + nums[i] >= goal):
                return True
            elif i + nums[i] >= goal:
                goal = i
            i -=1
        return False
# Given integer array nums
# initially positioned at arrays first index
    # each element represents your max jump length at that pos
    # Return true if you can reach last index or false otherwise
