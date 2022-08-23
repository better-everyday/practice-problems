"""
--- Description ---

Given the root of a binary tree, invert the tree, and return its root.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        t = root
        while t:
            temp = t.left
            t.left = t.right
            t.right = temp

            self.invertTree(t.left)
            self.invertTree(t.right)
            return t

"""
--- Submission ---

Runtime: 37 ms, faster than 83.10% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 12.26% of Python3 online submissions for Invert Binary Tree.
"""