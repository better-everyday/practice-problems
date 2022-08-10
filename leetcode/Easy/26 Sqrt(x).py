"""
--- Description ---

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part 
of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

"""
--- Submission ---

Runtime: 39 ms, faster than 92.11% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.9 MB, less than 10.89% of Python3 online submissions for Sqrt(x).
"""