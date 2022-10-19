"""
--- Description ---

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        list = sorted(nums1 + nums2)
        print(list)
        if len(list) % 2 == 0:
            index = len(list)//2
            return (list[index]+list[index-1])/2
        else:
            return list[len(list)//2]

"""
--- Submission ---

Runtime: 184 ms, faster than 54.64% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 67.23% of Python3 online submissions for Median of Two Sorted Arrays.
"""