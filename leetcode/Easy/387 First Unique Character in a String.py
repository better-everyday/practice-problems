"""
--- Description ---

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # 1
        """
        x = s
        while x:
            print(x)
            if not x[0] in x[1:]:
                return s.index(x[0])
            x = [i for i in x if i != x[0]]
            if len(x) == 1:
                return s.index(x[0])

        return -1
        """

        # 2
        for i in s:
            if s.count(0) == 1:
                return s.index(i)
        return -1

obj = Solution()
print(obj.firstUniqChar("aabb"))

"""
--- Submission ---

1.
Runtime: 719 ms, faster than 11.15% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.7 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.

2.
Runtime: 7579 ms, faster than 5.00% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 16.77% of Python3 online submissions for First Unique Character in a String.
"""