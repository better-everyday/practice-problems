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

        # 1
        # return int(math.sqrt(x))


        # 2. Brute Force
        # s = 0
        # while True:
        #     if (s + 1)**2 > x:
        #         return s
        #     s += 1

        # 3. Binary Search
        left, right = 0, 436340
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if (mid + 1)**2 > x:
                if (mid)**2 > x:
                    right = mid - 1
                else:
                    return int(mid)
            else:
                left = mid + 1
                    
obj = Solution()
print(obj.mySqrt(4))

"""
--- Submission ---

1. 
Runtime: 39 ms, faster than 92.11% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.9 MB, less than 10.89% of Python3 online submissions for Sqrt(x).

2. Brute Force
Runtime: 8508 ms, faster than 5.00% of Python3 online submissions for Sqrt(x).      O(n)
Memory Usage: 13.8 MB, less than 96.36% of Python3 online submissions for Sqrt(x).  O(1)

3. Binary Search
Runtime: 43 ms, faster than 86.17% of Python3 online submissions for Sqrt(x).       O(logn)
Memory Usage: 13.8 MB, less than 57.11% of Python3 online submissions for Sqrt(x).  O(1)
"""