# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def nodeFound(root, finding):
            if root == None: return False
            if root == finding: return True
            
            return nodeFound(root.left, finding) or nodeFound(root.right, finding)

        def LCA(root):
            if root == None: return None
            
            if root == p:
                if nodeFound(root.left, q) or nodeFound(root.right, q):
                    return root
            elif root == q:
                if nodeFound(root.left, p) or nodeFound(root.right, p):
                    return root
            else:
                if (nodeFound(root.left, p) and nodeFound(root.right, q)) or (nodeFound(root.left, q) and nodeFound(root.right, p)):
                    return root

            left = LCA(root.left)
            if left != None:
                return left
            return LCA(root.right)

        return LCA(root)