"""
Observation 1: nums1 is essentially nums1[:m]
Observation 2: only the indexes of nums1 can be modified

Problem 1: How to modify nums1 indexes efficiently

Solution 1: 
- Two pointers from start of nums1[:m] and nums2
- loop over these two until end
- every loop, take smaller of two pointers and place in secondary array, then increment
- after n+m iterations, loop through secondary array and modify nums1 indices

Insight 1: 
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        i = 0
        j = 0
        while i < m or j < n:
            if i == m:
                sorted.append(nums2[j])
                j += 1
                continue
            elif j == n:
                sorted.append(nums1[:m][i])
                i += 1
                continue

            if nums1[:m][i] <= nums2[j]:
                sorted.append(nums1[:m][i])
                i += 1
                continue
            else:
                sorted.append(nums2[j])
                j += 1
                continue

        for i, num in enumerate(sorted):
            nums1[i] = num