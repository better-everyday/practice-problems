# type: ignore
"""
--- Description ---

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                if isBadVersion(mid - 1):
                    right = mid - 1
                else:
                    return mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1
                    
        return right

"""
--- Submission ---

Runtime: 28 ms, faster than 96.20% of Python3 online submissions for First Bad Version.
Memory Usage: 14 MB, less than 12.71% of Python3 online submissions for First Bad Version.
"""