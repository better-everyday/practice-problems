"""
--- Description ---

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear 
as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        list = []
        for x in nums1:
            if x in nums2:
                list.append(x)
                nums2.remove(x)

        return list

"""
--- Submission ---

Runtime: 61 ms, faster than 80.26% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 50.59% of Python3 online submissions for Intersection of Two Arrays II.
"""