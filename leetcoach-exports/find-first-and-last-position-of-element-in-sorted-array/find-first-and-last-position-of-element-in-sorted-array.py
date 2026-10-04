class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        l, r = 0, len(nums) - 1
        starting = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                starting = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if starting == -1:
            return [-1, -1]
        else:
            starting = l


        # Invariant; everything to the right of r, including r, is bigger than or equal to target
        # Everything to left is l is smaller than target

        # invariant; same as above. just manipulate it to be everything to left of l is smaller than or equal to
        l, r = 0, len(nums) - 1
        ending = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        ending = r
        return [starting, ending]
        
# Given array of integers
    # Sorted in ascending order
    # Find starting and ending position of a given target value

    # If target not found, return -1 -1
    # Log n
    # clearly bin search

# Run binary search twice would be my guess
    # find starting
    # find ending
