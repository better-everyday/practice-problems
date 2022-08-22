"""
--- Description ---

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root:
            if root.left == None and root.right == None:
                return 1

            left = 1 + self.minDepth(root.left)
            right = 1 + self.minDepth(root.right)

            if root.left != None and root.right != None:
                return left if left < right else right
            elif not root.left:
                return right
            else:
                return left
        return 0

"""
--- Submission ---

Runtime: 647 ms, faster than 82.28% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 54.7 MB, less than 34.46% of Python3 online submissions for Minimum Depth of Binary Tree.
"""