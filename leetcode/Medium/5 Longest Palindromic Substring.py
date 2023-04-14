"""
--- Description ---

Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = s[0]

        for ind, letter in enumerate(s):
            sub = s[ind:][0:s[ind:].rindex(letter)+1]
            while len(sub) >= len(pal):
                if sub == sub[::-1]:
                    pal = sub
                    break
                sub = sub[0:-1][0:sub.rindex(letter)+1]

        return pal

"""
--- Submission ---

Runtime: 849 ms, 44.6%
Memory: 13.9 MB, 53.43%
"""