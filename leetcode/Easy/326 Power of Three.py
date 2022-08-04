# type:ignore
from math import log
from tkinter.font import nametofont
"""
--- Description ---

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Loop
        if n < 1 or n == 2:
            return False
        while n != 1:
            if not n % 1 == 0:
                return False
            n /= 3
        return True

obj = Solution
if obj.isPowerOfThree(obj, 243):
    print(True)
else:
    print(False)


"""
--- Submission ---

1. Loop
Runtime: 122 ms, faster than 63.12% of Python3 online submissions for Power of Three.
Memory Usage: 13.8 MB, less than 57.78% of Python3 online submissions for Power of Three.
"""