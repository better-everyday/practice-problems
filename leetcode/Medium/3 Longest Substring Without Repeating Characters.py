"""
--- Description ---

Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 1. Brute Force
        """
        def find(seq):
            list = []
            for x in seq:
                if x not in list:
                    list.append(x)
                else:
                    break
            return list

        length = 0
        s = list(s)
        
        print(s)
        for x in range(len(s)):
            print(find(s[x:]))
            string = len(find(s[x:]))
            if string > length:
                length = string
            if length >= len(s) - x:
                break
        
        return length
        """

        # 2


obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))

"""
--- Submission ---

1. Brute Force
Runtime: 4144 ms, faster than 5.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 5.33% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
