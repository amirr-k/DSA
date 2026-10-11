class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[r]:
                 # we're in the sorted half:
                return min(res, nums[l])

            mid = (l + r) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1
        
        return res
        
# [6,7,0,1,3, 4, 5]
# Want to land on 0
    # start at 4, 2
    # if l > r, left is stuck in left half
    # then move left to mid + 1
    # if l < r, 
        # r - mid - 1

        
# Array of length n
# Ascending order
# Rotated between 1 and n times
    # Return minimum element
# Run binary search twice
# First find the minimum element