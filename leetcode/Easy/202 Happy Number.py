"""
--- Description ---

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def op(n):
            squares = []
            while n:
                n, x = divmod(n, 10)
                squares.append(x**2)
            return sum(squares)

        a = b = n
        
        while True:
            a = op(a)
            b = op(op(b))

            if b == 1:
                return True
            elif a == b:
                return False

"""
--- Submission ---

Runtime: 36 ms, faster than 92.44% of Python3 online submissions for Happy Number.
Memory Usage: 14 MB, less than 14.75% of Python3 online submissions for Happy Number.
"""