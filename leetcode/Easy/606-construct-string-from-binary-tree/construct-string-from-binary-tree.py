# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder_str(root):
        if root == None:
            return "()"
        
        string = str(root.val)
        string += "(" + preorder_str(root.left) + ")"
        string += "(" + preorder_str(root.right) + ")"
        return string

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = preorder_str(root)
        print(string)
        if root.left == None and root.right == None:
          return str(root.val)
        while "())" in string or ")()" in string:
            string = string.replace("())", ")")
            string = string.replace(")()", ")")
        return string