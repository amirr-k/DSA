class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l, r = 0, 0
        cost = 0
        res = 0
        while r < len(s):
            addCost = abs(ord(s[r]) - ord(t[r]))
            # Check if addition is valid
            cost += addCost
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(r - l + 1, res)
            r += 1
        return res
        
# Given two strings s and t of same length and int maxCost


# Change s to t

# Changing ith character of s to ith character of t costs s[i] - t[i]

# 