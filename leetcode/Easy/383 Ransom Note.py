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


"""