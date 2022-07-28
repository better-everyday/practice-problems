# type: ignore
"""
--- Description ---

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in nums:
            if i != nums.index(i):
                return i-1
        return len(nums)

"""
--- Submission ---

Runtime: 2534 ms, faster than 13.22% of Python3 online submissions for Missing Number.
Memory Usage: 15.1 MB, less than 76.43% of Python3 online submissions for Missing Number.
"""