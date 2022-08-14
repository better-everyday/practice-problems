"""
--- Description ---

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down 
to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def traverse(root):
            l = 0
            r = 0
            
            if root.left != None:
                l = 1 + traverse(root.left)
            if root.right != None:
                r = 1 + traverse(root.right)

            if l >= r: return l
            else: return r

        if root:
            return traverse(root)

        return 0

"""
--- Submission ---

Runtime: 49 ms, faster than 83.21% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.2 MB, less than 74.83% of Python3 online submissions for Maximum Depth of Binary Tree.
"""