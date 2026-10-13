class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid >= 1 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                # 1, 2, 3, 4, 3, 6
                l = mid + 1
            else:
                return mid
        return mid
# [1,2,3,1]
# 0, 3
# mid == 1 == number 2
# l = mid + 1 == 2
# l = 2, r = 3
# 5 // 2 = 2
# mid == 2
    # 


# [1,2,1,3,2]
# mid == 2
    # 

        

    
# Always move towards greater using binary search
    # [1, 2, 1, 3, 2]
    # l, r = 0, 4
    # mid == 2
    # r = 1
    # l, r = 0, 1
    # mid == 0
    # 