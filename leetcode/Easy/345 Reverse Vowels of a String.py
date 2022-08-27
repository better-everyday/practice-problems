"""
--- Description ---

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        # 1 List O(n)
        """
        s = list(s)
        left, right = 0, -1
        vowels = "aeiouAEIOU"

        for x in range(len(s)):
            if left >= len(s)+right+1:
                break
            
            if not s[left] in vowels:
                left += 1
                continue
            if not s[right] in vowels:
                right -= 1
                continue
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        return "".join(s)
        """

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

        # 3 O(logn)


"""
--- Submission ---

1.
Runtime: 55 ms, faster than 92.64% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15 MB, less than 82.31% of Python3 online submissions for Reverse Vowels of a String.

2.
Runtime: 117 ms, faster than 27.34% of Python3 online submissions for Reverse Vowels of a String.       O(n)
Memory Usage: 14.7 MB, less than 93.39% of Python3 online submissions for Reverse Vowels of a String.   O(1)
"""