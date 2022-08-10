"""
--- Description ---

Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.pop(nums.index(num))
        return len(nums)

obj = Solution()
print(obj.removeDuplicates([0, 1, 1, 1, 1]))

"""
--- Submission ---


"""