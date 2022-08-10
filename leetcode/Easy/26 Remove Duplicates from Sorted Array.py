"""
--- Description ---

Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # 1
        # for num in nums:
        #     while nums.count(num) > 1:
        #         nums.remove(num)
        # return len(nums)


        # 2
        i = 1
        for num in nums[1::]:
            if num == nums[i-1]:
                nums.pop(i-1)
                i -= 1
            i += 1
            
        return len(nums)

obj = Solution()
print(obj.removeDuplicates([0, 1, 1, 1, 1]))

"""
--- Submission ---

1.
Runtime: 5260 ms, faster than 5.02% of Python3 online submissions for Remove Duplicates from Sorted Array.      O(n^2)/O(nlogn)???
Memory Usage: 15.6 MB, less than 16.41% of Python3 online submissions for Remove Duplicates from Sorted Array.

2. 
Runtime: 145 ms, faster than 54.28% of Python3 online submissions for Remove Duplicates from Sorted Array.      O(n)
Memory Usage: 15.5 MB, less than 61.41% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""