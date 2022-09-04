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

        # 2 O(n)
        """
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
        """

        # 3
        """
        x = s
        while len(x) > 0:
            if s.count(x[0]) > 1:
                x = x.replace(x[0], "")
            else:
                return s.index(x[0])
        return -1
        """

        # 4
        m = math.pow(10,5);     #min
        
        for c in alc:
            try:
                tmp = s.index(c)
                tmp2 = s.rindex(c)
            except: 
                continue;
                
            if tmp == tmp2:
                m = tmp if tmp<m else m
                
        return -1 if m == math.pow(10,5) else m

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

3.
Runtime: 58 ms, faster than 99.13% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.1 MB, less than 95.37% of Python3 online submissions for First Unique Character in a String.

4.
Runtime: 30 ms, faster than 99.99% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 16.77% of Python3 online submissions for First Unique Character in a String.
"""