class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        mp = {}
        mp[0] = -1
        cnt = 0 
        for i, num in enumerate(nums):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            # Check
            if cnt in mp:
                maxLen = max(maxLen, i - mp[cnt])
            if cnt not in mp:
                mp[cnt] = i
        return maxLen
# [0,1,1,1,1,1,0,0,0]

# maxLen = 0 
# mp = {}
# cnt = 0

# [0, 1]
# mp[-1] = 0
# mp[0] = 1

# mp[1] = 2

# end becomes [0,1,1,1,1,1,0,0,0]
# cnt == -1 + 5 * 1 - 3 * 1
# = -1 + 5 - 3
# 1
# 

# if 0 - cnt in mp:
               # maxLen = max(maxLen, i - mp[(0 - cnt)])


# Given binary array nums
# return the max length of a contigous subarray with an equal number of 
# 0 and 1

# 