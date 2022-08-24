"""
--- Description ---

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in 
the binary representation of i.
"""

from math import log, floor

class Solution:
    def countBits(self, n: int) -> list[int]:
        
        # 1. Slow version   O(nlogn)
        def binary_count(n):
            ones = 0
            while n > 0:
                n -= 2**floor(log(n, 2))
                ones += 1
            return ones

        list = []
        for x in range(n+1):
            list.append(binary_count(x))
        return list

"""
--- Submission ---


"""