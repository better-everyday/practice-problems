"""
--- Description ---

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" 
while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for x in t:
            if not s:
                break
            if not s[0] in t:
                return False
            if x == s[0]:
                s = s[1:]
        if len(s) == 0:
            return True

"""
--- Submission ---

Runtime: 35 ms, faster than 89.89% of Python3 online submissions for Is Subsequence.
Memory Usage: 13.9 MB, less than 42.80% of Python3 online submissions for Is Subsequence.
"""