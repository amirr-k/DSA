class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        res = 0
        peak = prices[0]
        buy = prices[0]
        for price in prices:
            if price > peak:
                peak = price
            elif price < buy or (peak - price > fee):
                res += max(0, peak - buy - fee)
                buy = price
                peak = price
            else:
                continue
        res += max(0, peak - buy - fee)

        return res
# Given an array prices
    # Prices[i] is the price of a given stock on the ith day
    # Integer fee representing transaction fee

# Find max profit you can achieve
    # Greedy SHOULD be to maximize profit at every step
    # At every step
        1. 

