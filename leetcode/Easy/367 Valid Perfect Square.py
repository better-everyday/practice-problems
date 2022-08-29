"""
--- Description ---

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left, right = 0, 436340
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid**2 < num:
                left = mid
            elif mid**2 > num:
                right = mid
            else:
                return True

"""
--- Submission ---

Runtime: 24 ms, faster than 99.42% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.8 MB, less than 55.83% of Python3 online submissions for Valid Perfect Square.
"""