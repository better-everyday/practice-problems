"""
--- Description ---

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in 
the binary representation of i.
"""

from math import log, floor

class Solution:
    def countBits(self, n: int) -> list[int]:
        
        # 1. Slow version   O(nlogn)
        """
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

        # 2. Binary conversion  O(n)
        list = []
        for x in range(n+1):
            list.append(bin(x)[2:].count("1"))
        return list

"""
--- Submission ---

1.
Runtime: 419 ms, faster than 5.05% of Python3 online submissions for Counting Bits.
Memory Usage: 20.9 MB, less than 30.64% of Python3 online submissions for Counting Bits.

2. 
Runtime: 98 ms, faster than 85.48% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 30.64% of Python3 online submissions for Counting Bits.
"""