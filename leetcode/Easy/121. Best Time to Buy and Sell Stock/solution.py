"""
--- Description ---

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0
        low = inf

        for n in prices:
            if n < low:
                low = n
            if n - low > profit:
                profit = n - low
        
        return profit

"""
--- Submission ---

Runtime: 954 ms, faster than 99.36% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 6.82% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""