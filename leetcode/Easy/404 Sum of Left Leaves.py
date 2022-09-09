"""
--- Description ---

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""

from subprocess import list2cmdline


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def add(root, list, split=""):
            if root.left == None and root.right == None and split == "left":
                list.append(root.val)
            if root.left != None:                
                add(root.left, list, "left")
            if root.right != None:
                add(root.right, list, "right")

        list = []
        add(root, list)

        return sum(list) if len(list) > 0 else 0

"""
--- Submission ---

Runtime: 36 ms, faster than 91.18% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.6 MB, less than 71.83% of Python3 online submissions for Sum of Left Leaves.
"""