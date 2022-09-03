"""
--- Description ---

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine 
and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.pop(magazine.index(i))
            else:
                return False
        return True

"""
--- Submission ---

Runtime: 64 ms, faster than 82.60% of Python3 online submissions for Ransom Note.
Memory Usage: 14.5 MB, less than 5.22% of Python3 online submissions for Ransom Note.
"""