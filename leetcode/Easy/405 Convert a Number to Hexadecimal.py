"""
--- Description ---

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two's complement 
method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer 
except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
"""

from math import log, floor


class Solution:
    def toHex(self, num: int) -> str:
        
        def convert(num):
            key = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
            string = ""

            digits = floor(log(num, 16))
            for x in range(digits):
                digit = 0
                while 16**digits * (digit + 1) <= num:
                    digit += 1
                string += key[digit]
                num -= 16**digits * digit
                digits -= 1
            if num:
                string += key[num]
            else:
                string += "0"
            return string

        if num > 0:
            string = convert(num)
        elif num < 0:
            converted = 4294967295 + num + 1
            string = convert(converted)
        else:
            return "0"

        return string

obj = Solution()
print(obj.toHex(64))
"""
--- Submission ---

Runtime: 29 ms, faster than 95.38% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 13.8 MB, less than 62.32% of Python3 online submissions for Convert a Number to Hexadecimal.
"""