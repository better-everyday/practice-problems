"""
--- Description ---

Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        for num in nums[1::]:
            if num == nums[i-1]:
                nums.pop(i-1)
                i -= 1
            i += 1
            print(i, nums)
            
        return len(nums)

obj = Solution()
print(obj.removeDuplicates([0, 1, 1, 1, 1]))

"""
--- Submission ---

1.
Runtime: 5260 ms, faster than 5.02% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 16.41% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""