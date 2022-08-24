"""
--- Description ---

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:

        def traverse(root, list, phrase):
            phrase += "->" + str(root.val)

            if root.left == None and root.right == None:
                phrase = phrase[2:]
                list.append(phrase)

            if root.left:
                traverse(root.left, list, phrase)
            if root.right:
                traverse(root.right, list, phrase)

        list = []
        phrase = ""
        traverse(root, list, phrase)

        return list

"""
--- Submission ---

Runtime: 32 ms, faster than 95.41% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.9 MB, less than 29.10% of Python3 online submissions for Binary Tree Paths.
"""