# type: ignore
"""
--- Description ---

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1 or n == 2 or n == 3 or n == 5:
            return True
        if n%2 == 0:
            n = n/2
            return self.isUgly(n)

        if n%3 == 0:
            n = n/3
            return self.isUgly(n)

        if n%5 ==0:
            n = n/5
            return self.isUgly(n)

        return False                                                                                                     

"""
--- Submission ---

Runtime: 41 ms, faster than 74.92% of Python3 online submissions for Ugly Number.
Memory Usage: 13.9 MB, less than 13.00% of Python3 online submissions for Ugly Number.
"""