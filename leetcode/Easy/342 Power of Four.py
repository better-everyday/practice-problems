"""
--- Description ---

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            if log(n, 4).is_integer():
                return True

"""
--- Submission ---

Runtime: 34 ms, faster than 91.81% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.
"""