"""
--- Description ---

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            targetSum -= root.val
            
            if abs(targetSum) < 0: return

            if root.left == None and root.right == None: return True if not targetSum else 0

            if self.hasPathSum(root.left, targetSum): return self.hasPathSum(root.left, targetSum)
            if self.hasPathSum(root.right, targetSum): return self.hasPathSum(root.right, targetSum)
        return
            
"""
--- Submission ---

Runtime: 67 ms, faster than 51.21% of Python3 online submissions for Path Sum.
Memory Usage: 15 MB, less than 57.83% of Python3 online submissions for Path Sum.
"""