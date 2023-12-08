"""
--- Description ---

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that 
is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = "13579"
        for i, x in enumerate(num[::-1]):
            if x in odd:
                if i == 0:
                    return num

                return num[:-1*i]
        return ""

"""
--- Submission ---

Runtime: 46ms [87.49%]
Memory: 17.67MB [96.57%]
"""