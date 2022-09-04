"""
--- Description ---

You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # 1. Counting (Counter method might be better)
        """
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for letter in alpha:
            if t.count(letter) > s.count(letter):
                return letter
        """
        
        # 2. Unicode
        asc,asc1=0,0
        for i in t:
            asc=asc+ord(i)
        for j in s:
            asc1=asc1+ord(j)
        asc=asc-asc1
        return chr(asc)

"""
--- Submission ---

Runtime: 41 ms, faster than 84.17% of Python3 online submissions for Find the Difference.
Memory Usage: 13.9 MB, less than 31.96% of Python3 online submissions for Find the Difference.
"""