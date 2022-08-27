"""
--- Description ---

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        # 1 List (WIP)
        s = list(s)
        left, right = 0, -1
        vowels = "aeiouAEIOU"

        count = 0
        while count < len([i for i in s if i in vowels])//2:
            while s[left] not in vowels:
                left += 1
            while s[right] not in vowels:
                right -= 1
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            count += 1
        
        return "".join(s)

        # 2 Adding
        """
        string = ""
        vowels = "aeiouAEIOU"

        strip = [i for i in s if i in vowels]
        for x in range(len(strip)//2):
            strip[x], strip[-x-1] = strip[-x-1], strip[x]

        for x in s:
            if x not in vowels:
                string += x
            else:
                string += strip.pop(0)

        return string
        """

        # 3

"""
--- Submission ---

Runtime: 117 ms, faster than 27.34% of Python3 online submissions for Reverse Vowels of a String.       O(n)
Memory Usage: 14.7 MB, less than 93.39% of Python3 online submissions for Reverse Vowels of a String.   O(1)
"""