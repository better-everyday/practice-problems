# type:ignore
"""
--- Description ---

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Iterate through array and remove all zeroes, then append zeroes to end
        # count = nums.count(0)
        # nums = list(filter(lambda a: a != 0, nums))
        # for i in range(count):
        #     nums.append(0)
        # Apparently this doesn't work because we have to do swapping

        # Find first non-zero number by getting a reference from a list without zeroes and swap with the first zeri
        # ordered = 0
        # if nums.count(0) != 0:
        #     while (len(nums) - nums.count(0)) != ordered:
        #         nonzero = list(filter(lambda a: a != 0, nums))

        #         first_nonzero = nums.index(nonzero[ordered])
        #         first_zero = nums.index(0)

        #         if first_nonzero > first_zero:
        #             nums[first_zero], nums[first_nonzero] = nums[first_nonzero], nums[first_zero]

        #         ordered += 1
        # This method does not work either because the question was unclear on whether there could be duplicates in the array

        # Find first non-zero iteratively
        # ordered = 0
        # if nums.count(0) != 0:
        #     for i in range(len(nums)):
        #         if nums[ordered] != 0 and ordered > nums.index(0):
        #             nums[nums.index(0)], nums[ordered] = nums[ordered], nums[nums.index(0)]
        #         ordered += 1

        # I just found out that you don't have to use swap; you can do array transformations but not reassignments
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

"""
--- Submission ---

1. 
Runtime: 7443 ms, faster than 5.01% of Python3 online submissions for Move Zeroes.  Time: O(n)
Memory Usage: 15.4 MB, less than 96.90% of Python3 online submissions for Move Zeroes.  Space: O(1)

2.
Runtime: 632 ms, faster than 17.74% of Python3 online submissions for Move Zeroes. Time: O(n)
Memory Usage: 15.5 MB, less than 65.60% of Python3 online submissions for Move Zeroes. Space: O(1)
"""