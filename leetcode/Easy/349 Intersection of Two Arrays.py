"""
--- Description ---

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique 
and you may return the result in any order.
"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        return list(set([i for i in nums1 if i in nums2]))

"""
--- Submission ---

Runtime: 64 ms, faster than 73.28% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14 MB, less than 91.04% of Python3 online submissions for Intersection of Two Arrays.
"""