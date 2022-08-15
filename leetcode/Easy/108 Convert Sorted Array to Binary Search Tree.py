"""
--- Description ---

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node 
never differs by more than one.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: int) -> TreeNode:

        def add(elem, root):
            if root == None: 
                return TreeNode(elem)

            if elem < root.val:
                root.left = add(elem, root.left)
                return root
            else:
                root.right = add(elem, root.right)
                return root


        def binary_add(left, right, root, nums):
            if left < right:
                mid = (left + right) // 2
                root = add(nums[mid], root)

                binary_add(left, mid, root, nums)
                binary_add(mid+1, right, root, nums)
            return root

        root = None
        root = binary_add(0, len(nums), root, nums)
        return root

"""
--- Submission ---

Runtime: 74 ms, faster than 85.89% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 83.29% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""