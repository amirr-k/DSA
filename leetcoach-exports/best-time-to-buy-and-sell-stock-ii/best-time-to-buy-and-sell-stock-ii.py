class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        if len(prices) == 1:
            return res
        l, r = 0, 1
        currentTransaction = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                currentTransaction = max(currentTransaction, prices[r] - prices[l])
            if prices[r] < prices[r - 1]:
                l = r
                res += currentTransaction
                currentTransaction = 0
            r += 1
        res += currentTransaction
        return res
# [7,1,5,3,6,4]
# [7, 1]
# l = 0, r = 1
# if prices[r] < prices[r - 1] == True
# l = 1, r = 2
# res = 0
# [1, 5]
# prices[r] > prices[l] == True
# currentTransaction = 4 
# [1, 5, 3]
# l = 1, r = 3
# dip. prices[r] < prices[r - 1] == True
# l = r, r += 1
# l = 3, r = 4
# [3, 6]
# if prices[r] > prices[l] == True
# prices[r] - prices[l] = 3
# l = 3, r = 5
# 3, 6, 4
# 


# [9, 2, 3, 4, 6, 8, 3, 9]
# Buy on 2
# sell on 6
    # first if covers
# then buy on 3. 
    # [7,1,5,3,6,4]
    # l = 0, r = 1
    # l = r = 1, r += 1 = 2
    # so l = 1, r = 2
    # 
    # 
        
# Given int artay prices
# prices[i] is price of the stock on ith day

# On each day, you may decide to buy and/or sell the stock

# You can hold at most one share of the stock at any time


# You can sell and buy the stock multiple times on the same day,
# ensuring you never hold more than one share of the stock
