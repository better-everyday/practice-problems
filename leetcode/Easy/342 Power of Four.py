"""
--- Description ---

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # Cheat
        """
        if n > 0:
            if log(n, 4).is_integer():
                return True
        """
        
        # Proper
        # 4     16      64          256     1024    36?
        # 100   10000   1000000     100000000
        num = bin(n)[2:]
        return (num[0] == "1") and (num.count("0") % 2 == 0) and (num.count("1") == 1)

"""
--- Submission ---

# Cheat
Runtime: 34 ms, faster than 91.81% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.

# Proper
Runtime: 30 ms, faster than 96.09% of Python3 online submissions for Power of Four.
Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.
"""