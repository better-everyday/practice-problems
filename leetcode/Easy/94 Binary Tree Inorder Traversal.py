"""
--- Description ---

Given the root of a binary tree, return the inorder traversal of its nodes' values.
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Recursive
def inorder(inorder_list, root):
    if root == None:
        return

    inorder(inorder_list, root.left)
    inorder_list.append(root.val)
    inorder(inorder_list, root.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []
        inorder(inorder_list, root)
        return inorder_list
    
# Iterative


"""
--- Submission ---

Runtime:
Memory:
"""