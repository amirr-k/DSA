class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [float('inf') for i in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums) - 1) :
            numSteps = nums[i]
            for j in range(i + 1, numSteps + i + 1):
                if j >= len(nums):
                    break
                else:
                    dp[j] = min(1 + dp[i], dp[j])
        return dp[-1]




# [2,3,1,1,4]
# First jump can reach index 1 or 2. 
# Always greedily land on max(i + jumpVal)
# at any step, 

# Subproblem == max number of jumps to get to index i 
# Base case = initially at indexed 0 
    # So 0 jumps necessary
# First step
    # As long as >= 1
# Second step. 
    # Make the first jump, see where you land
    # 

        
# 0 indexed array of integers

# each element nums[i] represents the maximum length of a forward jump
# from index i 


# return minimum number of jumps
# you wil always be able to reach index n. 