# type:ignore
"""
--- Description ---

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s.
"""

from re import L


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # pattern_storage = {}
        # if len(pattern) != len(s.split()):
        #     return False
        # for iteration, letter in enumerate(pattern):
        #     if not letter in pattern_storage and not s.split()[iteration] in pattern_storage.values():
        #         pattern_storage[letter] = s.split()[iteration]
        #     else:
        #         if s.split()[iteration] in pattern_storage.values():
        #             key = [k for k, v in pattern_storage.items() if v == s.split()[iteration]]
        #             if key[0] != letter:
        #                 print(False)
        #         else:
        #             if s.split()[iteration] != pattern_storage[letter]:
        #                 print(False)
        # Apparently this method is slow as shit

"""
--- Submission ---

1.
Runtime: 96 ms, faster than 5.38% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 23.23% of Python3 online submissions for Word Pattern.

"""